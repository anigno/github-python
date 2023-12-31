import time
from threading import Thread
from typing import Optional

from Apps.uav_simulator.simulator.data_types.Location3d import Location3d
from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d
from Apps.uav_simulator.simulator.logic.simple_uav_actions import SimpleUavActions
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from common.generic_event import GenericEvent
from common.printable_params import PrintableParams

class UpdateEventArgs:
    def __init__(self, location, direction, remaining_flight_time):
        self.location: Location3d = location
        self.direction: Direction3d = direction
        self.remaining_flight_time: float = remaining_flight_time

class SimpleUavManager:
    IN_LOCATION_DISTANCE = 10.0

    def __init__(self, name: str, uav_params: UavParams, location: Location3d, update_interval=1.0):
        self._name = name
        self.uav_params = uav_params
        self._location = location
        self._destination = location
        self._velocity = self.uav_params.flight_velocity
        self._update_thread: Optional[Thread] = None
        self._previous_update_time = 0.0
        self._is_update_thread_run = False
        self._direction = Direction3d()
        self._remaining_flight_time = 0
        self._update_interval = update_interval
        self.on_update = GenericEvent(UpdateEventArgs, '')

    @property
    def name(self):
        return self._name

    def start(self):
        self._is_update_thread_run = True
        self._previous_update_time = time.time()
        self.reset_flight_time()
        self._update_thread = Thread(name='update', target=self._update_thread_start, daemon=True)
        self._update_thread.start()

    def stop(self):
        self._is_update_thread_run = False

    def set_destination(self, destination: Location3d):
        self._destination = destination

    def reset_flight_time(self):
        self._remaining_flight_time = self.uav_params.max_flight_time

    def __str__(self):
        return PrintableParams.to_string(self)

    def _update_thread_start(self):
        while self._is_update_thread_run:
            time.sleep(self._update_interval)
            new_update_time = time.time()
            delta_time = new_update_time - self._previous_update_time
            self._direction = SimpleUavActions.calculate_Direction(self._location, self._destination)
            distance = SimpleUavActions.calculate_distance(self._location, self._destination)
            if distance > SimpleUavManager.IN_LOCATION_DISTANCE:
                self._location = SimpleUavActions.calculate_new_location(self._location, self._direction,
                                                                         self._velocity, delta_time)
            self.on_update.raise_event(UpdateEventArgs(self._location, self._direction, self._remaining_flight_time))
            self._remaining_flight_time -= delta_time
            self._previous_update_time = new_update_time

if __name__ == '__main__':
    from Apps.uav_simulator.testings.draw_course import draw3d

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
