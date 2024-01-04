from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from communication.udp.message_base import MessageBase

class FlyToDestinationMessage(MessageBase):
    MESSAGE_TYPE = 1001

    def __init__(self, location: Location3d):
        super().__init__()
        self.location = location
