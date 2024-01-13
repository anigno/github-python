import logging
from logging import Logger
from typing import Dict
from Apps.uav_simulator.simulator.communication.grpc.messages_client import GrpcMessagesClient
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class UavGrpcClientsStore:
    """store grpc clients"""

    def __init__(self, logger: Logger):
        self._logger = logger
        self._clients_dict: Dict[str, GrpcMessagesClient] = {}

    def add_update_uav_comm_data(self, descriptor: str, uav_ip: str, uav_port: int) -> GrpcMessagesClient:
        ret = None
        if descriptor in self._clients_dict:
            ret = self._clients_dict[descriptor]
        client = GrpcMessagesClient(self._logger, uav_ip, uav_port)
        self._clients_dict[descriptor] = client
        return ret

    def remove_uav_comm_data(self, descriptor: str) -> GrpcMessagesClient:
        client = self._clients_dict[descriptor]
        del (self._clients_dict[descriptor])
        return client

    def get_uav_comm_data(self) -> Dict[str, GrpcMessagesClient]:
        return self._clients_dict.copy()

if __name__ == '__main__':
    logger1: Logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
    LoggingInitiatorByCode()
    store = UavGrpcClientsStore(logger1)
    store.add_update_uav_comm_data('uav1', 'ip1', 1001)
    store.add_update_uav_comm_data('uav1', 'ip1', 1001)
    print(store.get_uav_comm_data())
