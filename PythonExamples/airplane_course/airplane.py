import math

from PythonExamples.airplane_course.Location3d import Location3d
from PythonExamples.airplane_course.direction3d import Direction3d

class Airplane:
    def __init__(self, name: str, location: Location3d, direction: Direction3d, max_direction_delta: Direction3d, velocity=0.0):
        self.name = name
        self.location = location
        self.direction = direction
        self.max_direction_delta = max_direction_delta
        self.velocity = velocity

    def move_next(self, interval_sec):
        self.location.x = self.location.x + math.cos(self.direction.azimuth) * math.cos(self.direction.elevation) * self.velocity * interval_sec
        self.location.y = self.location.y + math.sin(self.direction.azimuth) * math.cos(self.direction.elevation) * self.velocity * interval_sec
        self.location.h = self.location.h + math.sin(self.direction.elevation) * self.velocity * interval_sec

    def move_next_to_point(self, interval_sec, location: Location3d):
        dx = location.x - self.location.x
        dy = location.y - self.location.y
        dh = location.h - self.location.h
        dx = 0.000001 if dx == 0 else  dx
        req_az = math.atan(dy / dx)
        req_el = math.atan(dh / dx)
        self.direction.azimuth = req_az
        self.direction.elevation = req_el
        self.move_next(interval_sec)

    def __str__(self):
        str_list = []
        for v in self.__dict__:
            str_list.append(f'{v}:{self.__dict__[v]} ')
        return "".join(str_list)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    def test_move_next():
        global a
        a = Airplane('1 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        print(a)
        a.move_next(1.0)
        print(a)
        assert abs(a.location.x - 1) < 0.01
        a = Airplane('2 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.move_next(1.0)
        print(a)
        assert abs(a.location.y - 1) < 0.01
        a = Airplane('3 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        a.direction.elevation = math.pi / 4
        a.move_next(1.0)
        print(a)
        assert abs(a.location.x - 0.7071) < 0.01
        assert abs(a.location.h - 0.7071) < 0.01
        a = Airplane('4 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        a.direction.azimuth = math.pi / 4
        a.direction.elevation = math.pi / 4
        a.move_next(1.0)
        print(a)
        assert abs(a.location.x - 0.5) < 0.01
        assert abs(a.location.y - 0.5) < 0.01
        assert abs(a.location.h - 0.7071) < 0.01
        a = Airplane('5 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.direction.elevation = math.pi / 4
        a.move_next(1.0)
        print(a)
        assert abs(a.location.x - 0.0) < 0.01
        assert abs(a.location.y - 0.7071) < 0.01
        assert abs(a.location.h - 0.7071) < 0.01
        a = Airplane('6 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.direction.elevation = math.pi / 2
        a.move_next(1.0)
        print(a)
        assert abs(a.location.x - 0.0) < 0.01
        assert abs(a.location.y - 00) < 0.01
        assert abs(a.location.h - 1) < 0.01

    def test_move_to_point():
        a = Airplane('7 plane1', Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), Direction3d(), velocity=1.0)
        x = [a.location.x]
        y = [a.location.y]
        z = [a.location.h]

        for _ in range(200):
            a.move_next_to_point(1.0, Location3d(10, 0, 00))
            x.append(a.location.x)
            y.append(a.location.y)
            z.append(a.location.h)
            print(a.location)
        for _ in range(200):
            a.move_next_to_point(1.0, Location3d(10, 0, 0))
            x.append(a.location.x)
            y.append(a.location.y)
            z.append(a.location.h)
            print(a.location)

        # Create the figure and plot
        fig = plt.figure(figsize=(10, 6))
        ax = plt.axes(projection="3d")
        ax.plot3D(x, y, z, "blue", linewidth=2)

        # Set labels and title
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("3D Line Connecting Random Points")
        plt.show()

    test_move_next()
    test_move_to_point()
