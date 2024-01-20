from logging import Logger
from typing import Dict, Tuple

from Apps.uav_simulator.simulator.communication.http2.Http2Communicator import Http2Communicator
from Apps.uav_simulator.simulator.communication.messages.capabilities_update_message import CapabilitiesUpdateMessage
from Apps.uav_simulator.simulator.communication.messages.message_base import MessageBase, MessageTypeEnum
from Apps.uav_simulator.simulator.communication.messages.status_update_message import StatusUpdateMessage
from Apps.uav_simulator.simulator.communication.messages_factory import MessagesFactory
from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from common.generic_event import GenericEvent

class GroundControlCommunicator:
    def __init__(self, logger: Logger, messages_factory: MessagesFactory, local_ip, local_port):
        self.on_uav_status_updated = GenericEvent(StatusUpdateMessage)
        self.on_capabilities_updated = GenericEvent(CapabilitiesUpdateMessage)
        self.communicator = Http2Communicator(logger, messages_factory, local_ip, local_port)
        self.communicator.on_message_receive += self._on_message_received
        self.uav_comm_data: Dict[str, Tuple[str, int]] = {}

    def start(self):
        self.communicator.start()

    def send_fly_to_destination(self, uav_descriptor: str, destination: Location3d):
        pass

    def _on_message_received(self, message: MessageBase):
        if message.MESSAGE_TYPE == MessageTypeEnum.STATUS_UPDATE:
            message: StatusUpdateMessage
            self.uav_comm_data[message.uav_descriptor] = (ip, port)
            self.on_uav_status_updated.raise_event(message)
        elif message.MESSAGE_TYPE == MessageTypeEnum.CAPABILITIES_UPDATE:
            self.on_capabilities_updated.raise_event(message)
