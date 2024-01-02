import time
from threading import Thread, RLock
from typing import Optional
from Apps.uav_simulator.simulator.data_types.Location3d import Location3d
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus
from Apps.uav_simulator.simulator.event_args.update_event_args import UpdateEventArgs
from Apps.uav_simulator.simulator.logic.simple_uav_actions import SimpleUavActions
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from common.generic_event import GenericEvent
from common.printable_params import PrintableParams

class SimpleUavManager:
    IN_LOCATION_DISTANCE = 10.0

    def __init__(self, name: str, uav_params: UavParams, location: Location3d):
        self._name = name
        self.uav_params = uav_params
        self.uav_status = UavStatus(location)
        self._update_thread: Optional[Thread] = None
        self._is_update_thread_run = False
        self.on_update = GenericEvent(UpdateEventArgs)
        self._remaining_flight_time = 0.0

    @property
    def name(self):
        return self._name

    def start(self):
        self._is_update_thread_run = True
        # self._previous_update_time = time.time()
        self.reset_flight_time()
        self._update_thread = Thread(name='update', target=self._update_thread_start, daemon=True)
        self._update_thread.start()

    def stop(self):
        self._is_update_thread_run = False

    def set_destination(self, destination: Location3d):
        self.uav_status. = destination

    def reset_flight_time(self):
        with self.uav_status_locker:
            self._remaining_flight_time = self.uav_params.max_flight_time

    def __str__(self):
        return PrintableParams.to_string(self)

    def _update_thread_start(self):
        previous_update_time = time.time()
        while self._is_update_thread_run:
            time.sleep(self.uav_params.update_interval)
            new_update_time = time.time()
            delta_time = new_update_time - previous_update_time
            self._direction = SimpleUavActions.calculate_Direction(self._location, self._destination)
            distance = SimpleUavActions.calculate_distance(self._location, self._destination)
            if distance > SimpleUavManager.IN_LOCATION_DISTANCE:
                self._location = SimpleUavActions.calculate_new_location(self._location, self._direction,
                                                                         self.uav_params.flight_velocity, delta_time)
            self.on_update.raise_event(UpdateEventArgs(self._location, self._direction, self._remaining_flight_time))
            with self.uav_status_locker:
                self._remaining_flight_time -= delta_time

if __name__ == '__main__':
    x = []
    y = []
    z = []

    def on_update_event_handler(update_event_args: UpdateEventArgs):
        print(f'location={update_event_args.location} remaining={update_event_args.remaining_flight_time:.1f}s')
        x.append(update_event_args.location.x)
        y.append(update_event_args.location.y)
        z.append(update_event_args.location.h)

    uav = SimpleUavManager('uav1', UavParams(), Location3d(0, 0, 0), 0.5)
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
    # draw3d(x, y, z)
