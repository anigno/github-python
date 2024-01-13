import logging
from abc import ABC, abstractmethod
from logging import Logger
from typing import Dict, Tuple
from communication_service_pb2 import pStatusUpdate, pFlyToDestination, pResponse
from Apps.uav_simulator.simulator.communication.grpc.communication_service_pb2_grpc import CommunicationService
from Apps.uav_simulator.simulator.communication.grpc.messages_client import GrpcMessagesClient
from Apps.uav_simulator.simulator.communication.grpc.messages_server import GrpcMessagesServer
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class StatusUpdate:
    pass

class FlyToDestinationData:
    pass

class UavGrpcCommunicationData:
    def __init__(self):
        self.uav_comm_data: Dict[str, GrpcMessagesClient] = {}

    def add_update_uav_comm_data(self, descriptor: str, uav_ip: str, uav_port: int):
        client = GrpcMessagesClient(logger, uav_ip, uav_port)
        self.uav_comm_data[descriptor] = client

    def remove_uav_comm_data(self, descriptor: str):
        del (self.uav_comm_data[descriptor])

    def get_uav_comm_data(self) -> Dict[str, GrpcMessagesClient]:
        return self.uav_comm_data.copy()

class GroundControlCommunicator:
    """receives messages from all UAVs, and sends specific message to specific uav.
    exposes application data types from messages"""

    def __init__(self, logger: Logger, communicator_id: str, gc_ip: str, gc_port: int):
        self.logger = logger
        self.communicator_id = communicator_id
        self.gc_ip = gc_ip
        self.gc_port = gc_port
        self.uav_comm_data = UavGrpcCommunicationData()
        self.server = GrpcMessagesServer(logger, gc_ip, gc_port)
        self.server.on_StatusUpdateRequest += self.on_status_update_requested

    def start(self):
        self.server.start()

    def on_status_update_requested(self, status: pStatusUpdate):
        pass

    def fly_to_destination(self, uav_descriptor: str, mission_id: int, location: Location3d):
        message_id = GroundControlCommunicator.get_uniqueu_id()
        client = self.clients[uav_descriptor]
        client.send_fly_to_destination_request(message_id, mission_id, is_destination_home, location)

if __name__ == '__main__':
    logger1: Logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
    LoggingInitiatorByCode()

    c = Communicator(logger1, 'GC', '127.0.0.1', 10000)
