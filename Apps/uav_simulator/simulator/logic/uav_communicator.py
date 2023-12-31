from abc import ABC, abstractmethod

from common.generic_event import GenericEvent

class UavCommunicatorBase(ABC):
    def __init__(self):
        self.destination_received_event = GenericEvent()

    @abstractmethod
    def send_status(self, status_data):
        pass
