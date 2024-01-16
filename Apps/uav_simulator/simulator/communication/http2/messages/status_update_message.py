from Apps.uav_simulator.simulator.communication.http2.messages.message_base import MessageBase

class StatusUpdateMessage(MessageBase):
    def __init__(self):
        super().__init__()
        self.message_type=
