import time
from threading import Thread

from Apps.uav_simulator.simulator.data_types.Location3d import Location3d
from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d
from Apps.uav_simulator.simulator.logic.simple_uav_actions import SimpleUavActions
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams

class SimpleUavManager:
    IN_LOCATION_DISTANCE = 10

    def __init__(self, name: str, uav_params: UavParams, location: Location3d, direction: Direction3d):
        self.update_thread = Thread(name='update', target=self.update_thread_start, daemon=True)
        self.destination = self.uav_actions.location
        self.previous_update_time = 0.0

    def start(self):
        self.previous_update_time = time.time()
        self.update_thread.start()

    def fly_to(self, destination: Location3d):
        self.destination = destination
        self.uav_actions.direction = self.uav_actions.calculate_Direction_to(destination)

    def update_thread_start(self):
        time.sleep(1)
        new_update_time = time.time()
        delta_time = new_update_time - self.previous_update_time
        distance = self.uav_actions.calculate_distance_to(self.destination)
        if distance > SimpleUavManager.IN_LOCATION_DISTANCE:
            self.uav_actions.move(delta_time)
        self.previous_update_time = new_update_time
