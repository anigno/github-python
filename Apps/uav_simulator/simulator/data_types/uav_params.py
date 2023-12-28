class UavParams:
    def __init__(self, max_flight_time=60 * 5, max_velocity=10):
        self.max_flight_time = max_flight_time
        self.flight_velocity = max_velocity
        self.local_ip='127.0.0.1'
        self.local_port=7100
        self.buffer_size=60000


    def __str__(self):
        return f'({self.max_flight_time} {self.flight_velocity})'
