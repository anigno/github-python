from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d
from Apps.uav_simulator.simulator.data_types.location3d import Location3d

class UavStatus:
    """UAV current state parameters"""

    def __init__(self, location: Location3d):
        self.location: Location3d = location.new()
        self.destination: Location3d = location.new()
        self.direction = Direction3d()
        self.remaining_flight_time = 0
