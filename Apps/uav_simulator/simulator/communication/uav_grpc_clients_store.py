import logging
from logging import Logger
from typing import Dict

from Apps.uav_simulator.simulator.communication.grpc.messages_client import GrpcMessagesClient
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode
import grpc
class UavGrpcClientsStore:
    """store clients grpc client data"""

    def __init__(self, logger: Logger):
        self._logger = logger
        self._uav_comm_data: Dict[str, GrpcMessagesClient] = {}

    def add_update_uav_comm_data(self, descriptor: str, uav_ip: str, uav_port: int):
        client = GrpcMessagesClient(self._logger, uav_ip, uav_port)
        self._uav_comm_data[descriptor] = client

    def remove_uav_comm_data(self, descriptor: str) -> GrpcMessagesClient:
        client = self._uav_comm_data[descriptor]
        del (self._uav_comm_data[descriptor])
        return client

    def get_uav_comm_data(self) -> Dict[str, GrpcMessagesClient]:
        return self._uav_comm_data.copy()

if __name__ == '__main__':
    logger1: Logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
    LoggingInitiatorByCode()
    store = UavGrpcClientsStore(logger1)
    store.add_update_uav_comm_data('uav1', 'ip1', 1001)
    store.add_update_uav_comm_data('uav1', 'ip1', 1001)
    print(store.get_uav_comm_data())
