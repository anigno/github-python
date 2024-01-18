from typing import Dict, Callable

from Apps.uav_simulator.simulator.communication.messages.message_base import MessageBase

class MessagesFactory:
    def __init__(self):
        self._messages_dict: Dict[int, MessageBase] = {}

    def register_message(self, message_type):
        self._messages_dict[message_type.MESSAGE_TYPE.value] = message_type

    def create_message_instance(self, message_type_value: int, message_data_bytes: bytes) -> MessageBase:
        message_type = self._messages_dict[message_type_value]
        instance: MessageBase = message_type.__call__()
        instance.from_buffer(message_data_bytes)
        return instance
