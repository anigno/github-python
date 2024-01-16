import logging
from logging import Logger
from typing import Dict

from Apps.uav_simulator.simulator.communication.channel_base import ChannelBase

from Apps.uav_simulator.simulator.communication.http2.http2_server import Http2Server
from Apps.uav_simulator.simulator.communication.http2.messages.message_base import MessageTypeEnum
from Apps.uav_simulator.simulator.communication.http2.messages.status_update_message import StatusUpdateMessage
from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from common.generic_event import GenericEvent
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class ChannelData:
    def __init__(self, descriptor, ip, port):
        self.descriptor = descriptor
        self.ip = ip
        self.port = port

class GroundControlCommunicator:
    """receives messages from all UAVs, and sends specific message to specific uav."""

    def __init__(self, logger: Logger, communicator_id: str, local_ip: str, local_port: int):
        self.logger = logger
        self.communicator_id = communicator_id
        self.local_ip = local_ip
        self.local_port = local_port
        self.uav_channels: Dict[str, ChannelData] = {}
        self.server = Http2Server
        self.on_uav_status_receive = GenericEvent(StatusUpdateMessage)
        self.on_uav_capabilities_receive = GenericEvent(CapabilitiesUpdateMessage)
        self.server.on_request_post_received += self._on_request_post_received

    def start(self, local_ip, local_port):
        self.server.start(local_ip, local_port)

    def _on_request_post_received(self, data_dict: dict):
        # analize message type
        message_type = data_dict['message_type']
        if message_type == MessageTypeEnum.STATUS_UPDATE:
            self.handle_status_update_message(data_dict)
        elif message_type == MessageTypeEnum.CAPABILITIES_UPDATE:
            self.handle_capabilities_update_message(data_dict)
        if message_type == MessageTypeEnum.FLY_TO_DESTINATION:
            self.handle_fly_to_destination_message(data_dict)
        self.on_uav_status_receive.raise_event(status_update)

    def handle_status_update_message(self, data_dict: dict):
        # add channel if needed
        self.on_uav_status_receive.raise_event(StatusUpdateMessage())
        pass

    def send_fly_to_destination(self, uav_descriptor: str, mission_id: int, location: Location3d):
        client = self.uav_channels[uav_descriptor]

        client.send_fly_to_destination_request(message_id, mission_id, is_destination_home, location)

if __name__ == '__main__':
    logger1: Logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
    LoggingInitiatorByCode()

    c = GroundControlCommunicator(logger1, 'GC', '127.0.0.1', 10000)
