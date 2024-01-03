import time
from threading import Thread, RLock
from typing import Optional
from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus
from Apps.uav_simulator.simulator.event_args.update_event_args import UpdateEventArgs
from Apps.uav_simulator.simulator.logic.simple_uav_actions import SimpleUavActions
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from Apps.uav_simulator.testings.draw_course import draw3d
from common.crc.crc_providers import CrcProvider32Bit
from common.generic_event import GenericEvent
from common.printable_params import PrintableParams
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.udp_communication_manager import UdpCommunicationManager

class SimpleUavManager:

    def __init__(self, uav_params: UavParams, location: Location3d):
        self.uav_params = uav_params
        self.uav_status = UavStatus(location)
        self.status_locker = RLock()
        self._update_thread: Optional[Thread] = None
        self._is_update_thread_run = False
        self.on_update = GenericEvent(UpdateEventArgs)
        self.communicator = UdpCommunicationManager(uav_params.local_ip, uav_params.local_port, CrcProvider32Bit(), PickleMessageSerializer())

    def start(self):
        with self.status_locker:
            if self._is_update_thread_run:
                raise Exception('update thread is running')
            self._is_update_thread_run = True
        self.reset_flight_time()
        self._update_thread = Thread(name='update', target=self._update_thread_start, daemon=True)
        self._update_thread.start()

    def stop(self):
        with self.status_locker:
            self._is_update_thread_run = False

    def set_destination(self, destination: Location3d):
        with self.status_locker:
            self.uav_status.destination = destination.new()

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
            previous_update_time=new_update_time
            with self.status_locker:
                self.uav_status.direction = SimpleUavActions.calculate_Direction(self.uav_status.location, self.uav_status.destination)
                distance = SimpleUavActions.calculate_distance(self.uav_status.location, self.uav_status.destination)
                if distance > self.uav_params.in_location_distance:
                    self.uav_status.location = SimpleUavActions.calculate_new_location(self.uav_status.location, self.uav_status.direction,
                                                                                       self.uav_params.flight_velocity, delta_time)
                remaining_flight_time = self.uav_status.remaining_flight_time
                self.uav_status.remaining_flight_time -= delta_time
            self.on_update.raise_event(UpdateEventArgs(self.uav_status.location.new(), self.uav_status.direction.new(), remaining_flight_time))

if __name__ == '__main__':
    x = []
    y = []
    z = []

    def on_update_event_handler(update_event_args: UpdateEventArgs):
        print(f'location={update_event_args.location} remaining={update_event_args.remaining_flight_time:.1f}s')
        x.append(update_event_args.location.x)
        y.append(update_event_args.location.y)
        z.append(update_event_args.location.h)

    config = {'name': 'UAV01',
              'max_flight_time': 60 * 5,
              'flight_velocity': 10.0,
              'update_interval': 0.5,
              'in_location_distance': 10.0,
              'local_ip': '127.0.0.1',
              'local_port': 2001,
              'ground_control_ip': '127.0.0.1',
              'ground_control_port': 1000}
    uav = SimpleUavManager(UavParams(config), Location3d(0, 0, 0))
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
