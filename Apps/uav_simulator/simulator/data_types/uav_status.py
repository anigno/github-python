from threading import RLock
from Apps.uav_simulator.simulator.data_types import Location3d
from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d

class UavStatus:
    """UAV current state parameters"""

    def __init__(self, location: Location3d):
        self.locker = RLock()
        self.location: Location3d = Location3d(location)
        self.destination: location = Location3d(location)
        self.direction = Direction3d()
        self.remaining_flight_time = 0

    def update_location(self, location: Location3d):
        with self.locker:
            self.location.x = location.x
