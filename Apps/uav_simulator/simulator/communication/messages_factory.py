from abc import ABC, abstractmethod
from logging import Logger
from typing import Dict, Optional

from Apps.uav_simulator.simulator.communication.messages.message_base import MessageBase

class MessagesFactory(ABC):
    def __init__(self, logger: Logger):
        self._messages_dict: Dict[int, MessageBase] = {}
        self.logger = logger
        self.init_messages()

    def register_message(self, message_type):
        self._messages_dict[message_type.MESSAGE_TYPE.value] = message_type

    def create_message_instance(self, message_type_value: int, message_data_bytes: bytes) -> Optional[MessageBase]:
        try:
            message_type = self._messages_dict[message_type_value]
            instance = message_type.__call__()
            instance.from_buffer(message_data_bytes)
        except Exception as ex:
            self.logger.exception('', exc_info=ex)
            instance = None
        return instance

    @abstractmethod
    def init_messages(self):
        pass
