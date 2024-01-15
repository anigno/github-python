from abc import ABC, abstractmethod

class ChannelBase(ABC):
    @abstractmethod
    def create_channel(self, uav_ip, uav_port, *args, **kwargs):
        pass

    @abstractmethod
    def get_channel(self) -> any:
        pass
