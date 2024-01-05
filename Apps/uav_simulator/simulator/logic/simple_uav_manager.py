import logging
import time
from threading import Thread, RLock
from typing import Optional, List
from Apps.uav_simulator.simulator.capabilities.camera_simulation_capability import CameraSimulationCapability
from Apps.uav_simulator.simulator.capabilities.capability_base import CapabilityBase
from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus, FlightMode
from Apps.uav_simulator.simulator.event_args.update_event_args import UpdateEventArgs
from Apps.uav_simulator.simulator.messages.acknowledge_message import AcknowledgeMessage
from Apps.uav_simulator.simulator.messages.fly_to_destination_message import FlyToDestinationMessage
from Apps.uav_simulator.simulator.messages.ground_control_update_message import GroundControlUpdateMessage
from Apps.uav_simulator.simulator.logic.simple_uav_actions import SimpleUavActions
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from Apps.uav_simulator.simulator.messages.return_to_home_message import ReturnToHomeMessage
from common.crc.crc_providers import CrcProvider32Bit
from common.generic_event import GenericEvent
from common.printable_params import PrintableParams
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.udp_communication_manager import UdpCommunicationManager
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class SimpleUavManager:
    MESSAGES_READ_INTERVAL = 0.5

    def __init__(self, uav_params: UavParams, location: Location3d, capabilities: List[CapabilityBase]):
        logger.info(f'{uav_params}')
        self.uav_params = uav_params
        self.uav_status = UavStatus(location)
        self.status_locker = RLock()
        self._update_thread: Optional[Thread] = None
        self._messages_reading_thread: Optional[Thread] = None
        self._is_update_thread_run = False
        self.on_update = GenericEvent(UpdateEventArgs)
        self.communicator = UdpCommunicationManager(uav_params.uav_ip, uav_params.uav_port, CrcProvider32Bit(),
                                                    PickleMessageSerializer())
        self.capabilities = capabilities

    def start(self):
        with self.status_locker:
            if self._is_update_thread_run:
                raise Exception('update thread is running')
            self._is_update_thread_run = True
        self.reset_flight_time()
        self._update_thread = Thread(name='update', target=self._update_thread_start, daemon=True)
        self._update_thread.start()
        self._messages_reading_thread = Thread(name='receive', target=self._messages_reading_thread_start, daemon=True)
        self._messages_reading_thread.start()

    def stop(self):
        with self.status_locker:
            self._is_update_thread_run = False

    def set_destination(self, destination: Location3d):
        with self.status_locker:
            self.uav_status.destination = destination.new()

    def set_state(self, flight_mode: FlightMode):
        with self.status_locker:
            self.uav_status.flight_mode = flight_mode

    def reset_flight_time(self):
        with self.status_locker:
            self.uav_status.remaining_flight_time = self.uav_params.max_flight_time

    def __str__(self):
        return PrintableParams.to_string(self, True)

    def _update_thread_start(self):
        previous_update_time = time.time()
        while self._is_update_thread_run:
            time.sleep(self.uav_params.update_interval)
            new_update_time = time.time()
            delta_time = new_update_time - previous_update_time
            previous_update_time = new_update_time
            with self.status_locker:
                if not self.uav_status.flight_mode == FlightMode.IDLE:
                    self.uav_status.direction = SimpleUavActions.calculate_Direction(self.uav_status.location,
                                                                                     self.uav_status.destination)
                    distance = SimpleUavActions.calculate_distance(self.uav_status.location,
                                                                   self.uav_status.destination)
                    if distance > self.uav_params.in_location_distance:
                        self.uav_status.location = SimpleUavActions.calculate_new_location(
                            self.uav_status.location,
                            self.uav_status.direction,
                            self.uav_params.flight_velocity,
                            delta_time)
                    self.uav_status.remaining_flight_time -= delta_time
                capabilities_data = [capability.get(self.uav_status) for capability in self.capabilities]
                ground_control_message = GroundControlUpdateMessage(self.uav_params.name, self.uav_status,
                                                                    capabilities_data)
                self.communicator.send_to(self.uav_params.ground_control_ip, self.uav_params.ground_control_port,
                                          ground_control_message)
            self.on_update.raise_event(UpdateEventArgs(self.uav_status.location.new(), self.uav_status.direction.new(),
                                                       self.uav_status.remaining_flight_time, capabilities_data))

    def _messages_reading_thread_start(self):
        while self._is_update_thread_run:
            time.sleep(SimpleUavManager.MESSAGES_READ_INTERVAL)
            message_data_args = self.communicator.dequeue_received_message()
            logger.debug(f'{message_data_args.message.message_id} {message_data_args.message_type}')
            if message_data_args.message_type == FlyToDestinationMessage.MESSAGE_TYPE:
                message: FlyToDestinationMessage = message_data_args.message
                ack_message = AcknowledgeMessage(message.message_id)
                self.communicator.send_to(self.uav_params.ground_control_ip, self.uav_params.ground_control_port,
                                          ack_message)
                self.set_destination(message.location)
                self.set_state(FlightMode.TO_DESTINATION)
            if message_data_args.message_type == ReturnToHomeMessage.MESSAGE_TYPE:
                message: ReturnToHomeMessage = message_data_args.message
                ack_message = AcknowledgeMessage(message.message_id)
                self.communicator.send_to(self.uav_params.ground_control_ip, self.uav_params.ground_control_port,
                                          ack_message)
                self.set_destination(message.home_location)
                self.set_state(FlightMode.TO_HOME)

if __name__ == '__main__':
    from Apps.uav_simulator.testings.draw_course import draw3d
    from Apps.uav_simulator.testings.simple_uav_manager_config_samples import SimpleUavManagerConfigSamples

    LoggingInitiatorByCode()

    x = []
    y = []
    z = []

    def on_update_event_handler(update_event_args: UpdateEventArgs):
        print(f'location={update_event_args.location} remaining={update_event_args.remaining_flight_time:.1f}s')
        x.append(update_event_args.location.x)
        y.append(update_event_args.location.y)
        z.append(update_event_args.location.h)

    uav = SimpleUavManager(UavParams(SimpleUavManagerConfigSamples.config1), Location3d(0, 0, 0),
                           [CameraSimulationCapability()])
    print(uav)
    uav.on_update.register(on_update_event_handler)
    uav.start()
    time.sleep(2)
    uav.set_destination(Location3d(100, 100, 0))
    time.sleep(3)
    uav.set_destination(Location3d(100, 100, 100))
    time.sleep(3)
    uav.set_destination(Location3d(0, 0, 0))
    time.sleep(2)
    uav.stop()
    time.sleep(1)
    uav.start()
    time.sleep(6)
    draw3d(x, y, z)
