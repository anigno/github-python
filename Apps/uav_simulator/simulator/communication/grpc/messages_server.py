import logging
from logging import Logger
from threading import Thread
import grpc
from concurrent import futures
from Apps.uav_simulator.simulator.communication.grpc import communication_service_pb2_grpc
from common.generic_event import GenericEvent
from communication_service_pb2 import pStatusUpdate, pFlyToDestination, pResponse
from communication_service_pb2_grpc import CommunicationServiceServicer, add_CommunicationServiceServicer_to_server
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class MessagesServer(CommunicationServiceServicer):
    def __init__(self, logger: Logger, ip, port):
        self.logger = logger
        self.ip = ip
        self.port = port
        self.server_thread = None
        self.on_StatusUpdateRequest = GenericEvent(pStatusUpdate)
        self.on_FlyToDestinationRequest = GenericEvent(pFlyToDestination)
        self.logger.debug(f'MessagesServer init: {self.ip}:{self.port}')

    def StatusUpdateRequest(self, status_update, context):
        self.logger.debug(f"Received StatusUpdateRequest: {status_update}")
        response = pResponse(response_string="StatusUpdateRequest received")
        return response

    def FlyToDestinationRequest(self, fly_to_destination, context):
        self.logger.debug(f"Received FlyToDestinationRequest: {fly_to_destination}")
        response = pResponse(response_string="FlyToDestinationRequest received")
        return response

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        communication_service_pb2_grpc.add_CommunicationServiceServicer_to_server(self, server)
        server.add_insecure_port(f'{self.ip}:{self.port}')
        self.logger.debug("Communication Service Server started on port 50052")
        server.start()
        server.wait_for_termination()

    def start(self):
        self.server_thread = Thread(target=self.serve, daemon=True)
        self.server_thread.start()

if __name__ == '__main__':
    logger1: Logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
    LoggingInitiatorByCode()

    message_server = MessagesServer(logger1, 'localhost', 50052)
    message_server.start()
    input('exit')
