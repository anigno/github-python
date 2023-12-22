import math

from Apps.uav_simulator.simulator.Location3d import Location3d
from Apps.uav_simulator.simulator.direction3d import Direction3d
from Apps.uav_simulator.simulator.uav_params import UavParams

class SimpleUavActions:
    def __init__(self, name: str, uav_params: UavParams, location: Location3d, direction: Direction3d, velocity=0.0):
        self.name = name
        self.location = location
        self.direction = direction
        self.velocity = velocity
        self.flight_time = 0.0
        self.uav_params = uav_params

    def move(self, interval):
        self.location.x += math.cos(self.direction.azimuth) * math.cos(
            self.direction.elevation) * self.velocity * interval
        self.location.y += math.sin(self.direction.azimuth) * math.cos(
            self.direction.elevation) * self.velocity * interval
        self.location.h += math.sin(self.direction.elevation) * self.velocity * interval

    def calculate_Direction_to(self, location: Location3d) -> Direction3d:
        delta_x = location.x - self.location.x
        delta_y = location.y - self.location.y
        delta_z = location.h - self.location.h
        azimuth = math.atan2(delta_y, delta_x)
        horizontal_distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        elevation = math.atan2(delta_z, horizontal_distance)
        return Direction3d(azimuth, elevation)

    def calculate_distance_to(self, location: Location3d) -> float:
        distance = math.sqrt((location.x - self.location.x) ** 2 + (location.y - self.location.y) ** 2 + (
                location.h - self.location.h) ** 2)
        return distance

    def move_to(self, location: Location3d, interval: float):
        self.direction = self.calculate_Direction_to(location)
        self.move(interval)

    def __str__(self):
        str_list = []
        for v in self.__dict__:
            str_list.append(f'{v}:{self.__dict__[v]} ')
        return "".join(str_list)
