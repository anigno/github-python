from abc import ABC, abstractmethod
from logging import Logger

from Apps.uav_simulator.simulator.communication.http2.Http2Communicator import Http2Communicator
from Apps.uav_simulator.simulator.communication.messages.message_base import MessageBase
from Apps.uav_simulator.simulator.communication.messages.message_sent_fail_args import MessageSentFailsArgs
from Apps.uav_simulator.simulator.communication.messages_factory_base import MessagesFactoryBase
from common.generic_event import GenericEvent

class SpecializedCommunicatorBase(ABC):
    """base class for specialized purpose communicators (E.g. UavCommunicator)"""

    def __init__(self, logger: Logger, messages_factory: MessagesFactoryBase, local_ip, local_port):
        self.logger = logger
        self.communicator = Http2Communicator(logger, messages_factory, local_ip, local_port)
        self.on_error_sending_message = GenericEvent(MessageSentFailsArgs)
        self.communicator.on_message_receive += self._on_message_received

    def start(self):
        self.communicator.start()

    @abstractmethod
    def _on_message_received(self, message: MessageBase):
        pass
