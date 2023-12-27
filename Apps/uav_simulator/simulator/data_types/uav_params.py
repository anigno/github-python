class UavParams:
    def __init__(self, max_flight_time=60 * 5, max_velocity=10):
        self.max_flight_time = max_flight_time
        self.flight_velocity = max_velocity

    def __str__(self):
        return f'({self.max_flight_time} {self.flight_velocity})'
