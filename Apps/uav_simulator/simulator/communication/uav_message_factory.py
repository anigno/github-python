from Apps.uav_simulator.simulator.communication.messages.capabilities_update_message import CapabilitiesUpdateMessage
from Apps.uav_simulator.simulator.communication.messages.fly_to_destination_message import FlyToDestinationMessage
from Apps.uav_simulator.simulator.communication.messages.status_update_message import StatusUpdateMessage
from Apps.uav_simulator.simulator.communication.messages_factory import MessagesFactory

class UavSimulatorMessageFactory(MessagesFactory):
    def __init__(self):
        super().__init__()

    def init_messages(self):
        self.register_message(CapabilitiesUpdateMessage)
        self.register_message(FlyToDestinationMessage)
        self.register_message(StatusUpdateMessage)
