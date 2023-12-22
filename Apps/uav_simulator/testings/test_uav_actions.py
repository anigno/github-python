import math
import unittest

from Apps.uav_simulator.simulator.Location3d import Location3d
from Apps.uav_simulator.simulator.direction3d import Direction3d
from Apps.uav_simulator.simulator.simple_uav import SimpleUavActions
from Apps.uav_simulator.simulator.uav_params import UavParams

class TestUavActions(unittest.TestCase):

    def test_move(self):
        cos45 = math.cos(math.pi / 4)
        # move 1 second, azimuth=0 deg
        a = SimpleUavActions('1 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        # print(a)
        a.move(1.0)
        self.assertAlmostEqual(a.location.x, 1, 2)
        # move 1 second, azimuth=90 deg
        a = SimpleUavActions('2 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.move(1.0)
        self.assertAlmostEqual(a.location.y, 1, 2)
        # move 1 second, elevation=45 deg
        a = SimpleUavActions('3 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.elevation = math.pi / 4
        a.move(1.0)
        self.assertAlmostEqual(a.location.x, cos45, 2)
        self.assertAlmostEqual(a.location.h, cos45, 2)
        # move 1 second, azimuth=45 deg,elevation=45 deg
        a = SimpleUavActions('4 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 4
        a.direction.elevation = math.pi / 4
        a.move(1.0)
        self.assertAlmostEqual(a.location.x, 0.5, 2)
        self.assertAlmostEqual(a.location.y, 0.5, 2)
        self.assertAlmostEqual(a.location.h, cos45, 2)
        # move 1 second, azimuth=90 deg,elevation=45 deg
        a = SimpleUavActions('5 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.direction.elevation = math.pi / 4
        a.move(1.0)
        self.assertAlmostEqual(a.location.x, 0, 2)
        self.assertAlmostEqual(a.location.y, cos45, 2)
        self.assertAlmostEqual(a.location.h, cos45, 2)
        # move 1 second, azimuth=90 deg,elevation=90 deg
        a = SimpleUavActions('6 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.direction.azimuth = math.pi / 2
        a.direction.elevation = math.pi / 2
        a.move(1.0)
        self.assertAlmostEqual(a.location.x, 0, 2)
        self.assertAlmostEqual(a.location.y, 0, 2)
        self.assertAlmostEqual(a.location.h, 1, 2)

    def test_calculate_direction_to(self):
        # create uav at 0,0,0
        a = SimpleUavActions('1 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        # to 100,100
        location = a.calculate_Direction_to(Location3d(100, 100, 0))
        self.assertAlmostEqual(location.azimuth_degree, 45, 2)
        # to -100,-100
        location = a.calculate_Direction_to(Location3d(-100, -100, 0))
        self.assertAlmostEqual(location.azimuth_degree, -135, 2)
        # to 0,0,100
        location = a.calculate_Direction_to(Location3d(0, 0, 100))
        self.assertAlmostEqual(location.elevation_degree, 90, 2)
        # to 100,0,100
        location = a.calculate_Direction_to(Location3d(100, 0, 100))
        self.assertAlmostEqual(location.elevation_degree, 45, 2)
        # to 100,100, diagonal
        location = a.calculate_Direction_to(Location3d(100, 100, math.sqrt(100 ** 2 + 100 ** 2)))
        self.assertAlmostEqual(location.elevation_degree, 45, 2)
        # to 100,100,100
        location = a.calculate_Direction_to(Location3d(100, 100, 100))
        self.assertAlmostEqual(location.elevation_degree, 35.26, 2)

    def test_distance(self):
        # uav at 0,0,0
        a = SimpleUavActions('1 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        # distance to 100,0,0
        distance = a.calculate_distance_to(Location3d(100, 0, 0))
        self.assertAlmostEqual(distance, 100, 2)
        # distance to 100,100
        distance = a.calculate_distance_to(Location3d(100, 100, 0))
        self.assertAlmostEqual(distance, 141.42, 2)
        # distance to 100,100,100
        distance = a.calculate_distance_to(Location3d(100, 100, 100))
        self.assertAlmostEqual(distance, 173.205, 2)

    def test_move_to(self):
        a = SimpleUavActions('1 plane1', UavParams(), Location3d(0.0, 0.0, 0.0), Direction3d(0.0, 0.0), velocity=1.0)
        a.move_to(Location3d(100, 100, 100), 173.21)
        self.assertAlmostEqual(a.location.x, 100, 2)
        self.assertAlmostEqual(a.location.y, 100, 2)
        self.assertAlmostEqual(a.location.h, 100, 2)
