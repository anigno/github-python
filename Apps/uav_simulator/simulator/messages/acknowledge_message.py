from communication.udp.message_base import MessageBase

class AcknowledgeMessage(MessageBase):
    MESSAGE_TYPE = 101

    def __init__(self, message_id_for_ack: int):
        super().__init__()
        self.message_id_for_ack = message_id_for_ack
