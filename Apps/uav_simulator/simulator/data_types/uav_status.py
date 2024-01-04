from enum import Enum
from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d
from Apps.uav_simulator.simulator.data_types.location3d import Location3d

class FlightMode(Enum):
    IDLE = 0
    TO_DESTINATION = 1
    TO_HOME = 2

class UavStatus:
    """UAV current state parameters"""

    def __init__(self, location: Location3d):
        self.location: Location3d = location.new()
        self.destination: Location3d = location.new()
        self.direction = Direction3d()
        self.remaining_flight_time = 0
        self.flight_mode = FlightMode.IDLE
