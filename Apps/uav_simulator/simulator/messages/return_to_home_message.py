from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from communication.udp.message_base import MessageBase

class ReturnToHomeMessage(MessageBase):
    MESSAGE_TYPE = 1003

    def __init__(self, home_location: Location3d):
        super().__init__()
        self.home_location = home_location
