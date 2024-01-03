from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from Apps.uav_simulator.simulator.data_types.direction3d import Direction3d

class UpdateEventArgs:
    def __init__(self, location, direction, remaining_flight_time):
        self.location: Location3d = location
        self.direction: Direction3d = direction
        self.remaining_flight_time: float = remaining_flight_time
