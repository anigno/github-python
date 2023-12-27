import time
from threading import Thread

from Apps.uav_simulator.simulator.data_types.Location3d import Location3d
from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d
from Apps.uav_simulator.simulator.logic.simple_uav_actions import SimpleUavActions
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from common.generic_event import GenericEvent

class UpdateEventArgs:
    def __init__(self, location, direction, remaining_flight_time):
        self.location: Location3d = location
        self.direction: Direction3d = direction
        self.remaining_flight_time: float = remaining_flight_time

class SimpleUavManager:
    IN_LOCATION_DISTANCE = 10.0

    def __init__(self, name: str, uav_params: UavParams, location: Location3d):
        self._name = name
        self._uav_params = uav_params
        self._location = location
        self._destination = location
        self._velocity = self._uav_params.max_velocity * 0.8
        self._update_thread = Thread(name='update', target=self._update_thread_start, daemon=True)
        self._previous_update_time = 0.0
        self._is_update_thread_run = False
        self._direction = Direction3d()
        self.remaining_flight_time = self._uav_params.max_flight_time
        self.on_update = GenericEvent(UpdateEventArgs, '')

    @property
    def name(self):
        return self._name

    def start(self):
        self._is_update_thread_run = True
        self._previous_update_time = time.time()
        self._update_thread.start()

    def stop(self):
        self._is_update_thread_run = False

    def set_destination(self, destination: Location3d):
        self._destination = destination

    def __str__(self):
        s = ''
        for k in self.__dict__:
            s = s + f'{k}={str(self.__dict__[k])},'
        return s

    def _update_thread_start(self):
        while self._is_update_thread_run:
            time.sleep(1)
            new_update_time = time.time()
            delta_time = new_update_time - self._previous_update_time
            self._direction = SimpleUavActions.calculate_Direction(self._location, self._destination)
            distance = SimpleUavActions.calculate_distance(self._location, self._destination)
            if distance > SimpleUavManager.IN_LOCATION_DISTANCE:
                self._location = SimpleUavActions.calculate_new_location(self._location, self._direction, self._velocity, delta_time)
            self.on_update.raise_event(UpdateEventArgs(self._location, self._direction, self.remaining_flight_time))
            self.remaining_flight_time -= delta_time
            self._previous_update_time = new_update_time

if __name__ == '__main__':
    from Apps.uav_simulator.testings.draw_course import draw3d

    x = []
    y = []
    z = []

    def on_update_event_handler(update_event_args: UpdateEventArgs):
        print(f'location={update_event_args.location} remaining={update_event_args.remaining_flight_time}')
        x.append(update_event_args.location.x)
        y.append(update_event_args.location.y)
        z.append(update_event_args.location.h)

    uav = SimpleUavManager('uav1', UavParams(60, 5), Location3d(0, 0, 0))
    uav.on_update.register(on_update_event_handler)
    uav.start()
    time.sleep(2)
    uav.set_destination(Location3d(100, 100, 0))
    time.sleep(6)
    uav.set_destination(Location3d(100, 100, 100))
    time.sleep(6)
    uav.set_destination(Location3d(0, 0, 0))
    time.sleep(10)
    draw3d(x, y, z)
    input('enter to exit')
