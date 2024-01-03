from abc import ABC, abstractmethod

from Apps.uav_simulator.simulator.capabilities.capability_data import CapabilityData
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus

class CapabilityBase(ABC):
    @abstractmethod
    def get(self, uav_status: UavStatus) -> CapabilityData:
        pass
