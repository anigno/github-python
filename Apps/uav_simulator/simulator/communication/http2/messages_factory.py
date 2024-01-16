from typing import Dict

from Apps.uav_simulator.simulator.communication.http2.messages.message_base import MessageBase
from Apps.uav_simulator.simulator.communication.http2.messages.status_update_message import StatusUpdateMessage
from BL.meta_classes.no_instance_meta import NoInstanceMeta

class MessagesFactory(NoInstanceMeta):
    _messages_dict: Dict[int, MessageBase] = {}

    @staticmethod
    def init():
        MessagesFactory.register_message(StatusUpdateMessage)

    @staticmethod
    def register_message(message_type):
        MessagesFactory._messages_dict[message_type.MESSAGE_TYPE.value] = message_type

    @staticmethod
    def create_message_instance(message_type_value: int) -> MessageBase:
        message_type = MessagesFactory._messages_dict[message_type_value]
        instance = message_type()
        return instance
