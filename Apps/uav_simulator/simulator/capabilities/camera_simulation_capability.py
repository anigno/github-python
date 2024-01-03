from Apps.uav_simulator.simulator.capabilities.capability_base import CapabilityBase
from Apps.uav_simulator.simulator.capabilities.capability_data import CapabilityData
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus

class CameraSimulationCapability(CapabilityBase):
    def get(self, uav_status: UavStatus) -> CapabilityData:
        return CapabilityData('JPG', b'')
