from enum import Enum
from typing import Optional

from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d
from Apps.uav_simulator.simulator.data_types.location3d import Location3d

class FlightMode(Enum):
    IDLE = 0
    TO_DESTINATION = 1
    TO_HOME = 2

class UavStatus:
    """UAV current state parameters"""

    def __init__(self):
        self.location: Optional[Location3d] = None
        self.destination: Optional[Location3d] = None
        self.direction: Optional[Direction3d] = None
        self.remaining_flight_time = 0
        self.flight_mode = FlightMode.IDLE
