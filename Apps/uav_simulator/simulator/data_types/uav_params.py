import json

class UavParams:

    def __init__(self, uav_config: dict = None):
        self.descriptor = 'UAV01'
        self.max_flight_time = 5 * 60
        self.flight_velocity = 10
        self.local_ip = '127.0.0.1'
        self.local_port = 7100
        self.buffer_size = 60000
        self.ground_control_ip = '127.0.0.1'
        self.ground_control_port = 50000
        if uav_config:
            self._init_from_config(uav_config)

        def _init_from_config(config: dict):
            pass

    def __str__(self):
        return f'({self.max_flight_time} {self.flight_velocity})'
