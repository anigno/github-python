from Apps.uav_simulator.simulator.communication.messages.fly_to_destination_message import FlyToDestinationMessage
from common.generic_event import GenericEvent

class UavCommunicator:
    def __init__(self):
        self.on_fly_to_destination = GenericEvent(FlyToDestinationMessage)

    def send_uav_status(self):
        pass

    def send_uav_capabilities(self):
        pass
