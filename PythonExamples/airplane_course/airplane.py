import math

from PythonExamples.airplane_course.Location3d import Location3d
from PythonExamples.airplane_course.direction3d import Direction3d

class Airplane:
    def __init__(self, name: str, location: Location3d, direction: Direction3d, velocity=0.0):
        self.name = name
        self.location = location
        self.direction = direction
        self.velocity = velocity

    def move(self, interval_sec):
        self.location.x += math.cos(self.direction.azimuth) * math.cos(self.direction.elevation) * self.velocity * interval_sec
        self.location.y += math.sin(self.direction.azimuth) * math.cos(self.direction.elevation) * self.velocity * interval_sec
        self.location.h += math.sin(self.direction.elevation) * self.velocity * interval_sec

    def calculate_Direction(self, location: Location3d) -> Direction3d:
        delta_x = location.x - self.location.x
        delta_y = location.y - self.location.y
        delta_z = location.h - self.location.h
        azimuth = math.atan2(delta_y, delta_x)
        horizontal_distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        elevation = math.atan2(delta_z, horizontal_distance)
        return Direction3d(azimuth, elevation)

    def __str__(self):
        str_list = []
        for v in self.__dict__:
            str_list.append(f'{v}:{self.__dict__[v]} ')
        return "".join(str_list)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    epsilon = 0.01

    def test_move():
        a = Airplane('1 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        print(a)
        a.move(1.0)
        print(a)
        assert abs(a.location.x - 1) < epsilon
        a = Airplane('2 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.move(1.0)
        print(a)
        a = Airplane('3 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.elevation = math.pi / 4
        a.move(1.0)
        print(a)
        assert abs(a.location.x - 0.7071) < epsilon
        assert abs(a.location.h - 0.7071) < epsilon
        a = Airplane('4 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 4
        a.direction.elevation = math.pi / 4
        a.move(1.0)
        print(a)
        assert abs(a.location.x - 0.5) < epsilon
        assert abs(a.location.y - 0.5) < epsilon
        assert abs(a.location.h - 0.7071) < epsilon
        a = Airplane('5 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.direction.elevation = math.pi / 4
        a.move(1.0)
        print(a)
        assert abs(a.location.x - 0.0) < epsilon
        assert abs(a.location.y - 0.7071) < epsilon
        assert abs(a.location.h - 0.7071) < epsilon
        a = Airplane('6 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.direction.elevation = math.pi / 2
        a.move(1.0)
        print(a)
        assert abs(a.location.x - 0.0) < epsilon
        assert abs(a.location.y - 00) < epsilon
        assert abs(a.location.h - 1) < epsilon

    def test_calculate_direction():
        a = Airplane('1 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        print(a)
        location = a.calculate_Direction(Location3d(100, 100, 0))
        print(location)
        assert abs(location.azimuth_degree - 45) < epsilon
        location = a.calculate_Direction(Location3d(-100, -100, 0))
        print(location)
        assert abs(location.azimuth_degree - (-135)) < epsilon
        location = a.calculate_Direction(Location3d(0, 0, 100))
        print(location)
        assert abs(location.elevation_degree - 90) < epsilon
        location = a.calculate_Direction(Location3d(100, 0, 100))
        print(location)
        assert abs(location.elevation_degree - 45) < epsilon
        location = a.calculate_Direction(Location3d(100, 100, math.sqrt(100 ** 2 + 100 ** 2)))
        print(location)
        location = a.calculate_Direction(Location3d(100, 100, 100))
        print(location)
        assert abs(location.elevation_degree - 35.26) < epsilon

    test_move()
    test_calculate_direction()
