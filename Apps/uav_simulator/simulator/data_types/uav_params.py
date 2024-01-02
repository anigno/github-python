from common.printable_params import PrintableParams

class UavParams:
    """UAV constant values"""

    def __init__(self, uav_config: dict):
        self.name = uav_config['name']
        self.max_flight_time = uav_config['max_flight_time']
        self.flight_velocity = uav_config['flight_velocity']
        self.update_interval = uav_config['update_interval']
        # communication
        self.local_ip = uav_config['local_ip']
        self.local_port = uav_config['local_port']
        self.ground_control_ip = uav_config['ground_control_ip']
        self.ground_control_port = uav_config['ground_control_port']

    def __str__(self):
        return PrintableParams.to_string(self, True)

if __name__ == '__main__':
    config = {'name': 'UAV01',
              'max_flight_time': 60 * 5,
              'flight_velocity': 10.0,
              'update_interval': 0.5,
              'local_ip': '127.0.0.1',
              'local_port': 2001,
              'ground_control_ip': '127.0.0.1',
              'ground_control_port': 1000}
    params = UavParams(config)
    print(params)
