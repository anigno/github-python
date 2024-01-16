from Apps.uav_simulator.simulator.communication.http2.messages.message_base import MessageBase, MessageTypeEnum

class StatusUpdateMessage(MessageBase):
    MESSAGE_TYPE = MessageTypeEnum.STATUS_UPDATE

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()
