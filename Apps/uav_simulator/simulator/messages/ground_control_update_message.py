from typing import List
from Apps.uav_simulator.simulator.capabilities.capability_data import CapabilityData
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus
from communication.udp.message_base import MessageBase

class GroundControlUpdateMessage(MessageBase):
    MESSAGE_TYPE = 1002

    def __init__(self, uav_name: str, uav_status: UavStatus, capabilities_data: List[CapabilityData]):
        super().__init__()
        self.uav_name = uav_name
        self.uav_status = uav_status
        self.capabilities_data: List[CapabilityData] = capabilities_data
