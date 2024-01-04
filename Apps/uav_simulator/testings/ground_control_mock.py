import logging
from typing import List

from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from Apps.uav_simulator.simulator.messages.fly_to_destination_message import FlyToDestinationMessage
from Apps.uav_simulator.simulator.messages.ground_control_update_message import GroundControlUpdateMessage
from Apps.uav_simulator.simulator.logic.simple_uav_manager import SimpleUavManager
from Apps.uav_simulator.simulator.messages.return_to_home_message import ReturnToHomeMessage
from Apps.uav_simulator.testings.simple_uav_manager_config_samples import SimpleUavManagerConfigSamples
from common.crc.crc_providers import CrcProvider32Bit
from communication.udp.event_args.message_data_event_args import MessageDataEventArgs
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.udp_messages_communicator import UdpMessagesCommunicator
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class GroundControlMock:
    def __init__(self, uav_list: List[UavParams]):
        self.communicator = UdpMessagesCommunicator('127.0.0.1', 1000, CrcProvider32Bit(), PickleMessageSerializer())
        self.communicator.on_message_received += self.on_message_received
        self.uav_list = uav_list
        self.home_location = Location3d(0, 0, 0)

    def start(self):
        self.communicator.start_receiving()

    def fly_to(self, uav_params: UavParams, location):
        self.communicator.send_to(uav_params.uav_ip, uav_params.uav_port, FlyToDestinationMessage(location))

    def return_home(self):
        self.communicator.send_to(uav_params.uav_ip, uav_params.uav_port, ReturnToHomeMessage(self.home_location))

    def on_message_received(self, args: MessageDataEventArgs):
        if args.message_type == GroundControlUpdateMessage.MESSAGE_TYPE:
            message: GroundControlUpdateMessage = args.message
            logger.debug(f'{message.uav_name} {message.uav_status.flight_mode} {message.uav_status.location} {message.uav_status.remaining_flight_time}')

if __name__ == '__main__':
    import time

    LoggingInitiatorByCode()

    uav_params_list = [UavParams(params) for params in SimpleUavManagerConfigSamples.config_list]
    # create uavs
    for uav_params in uav_params_list:
        um = SimpleUavManager(uav_params, Location3d(0, 0, 0), [])
        um.start()

    gcm = GroundControlMock(uav_params_list)
    gcm.start()
    time.sleep(2)
    gcm.fly_to(uav_params_list[0], Location3d(100, 100, 100))
    time.sleep(10)
    gcm.return_home()
