import logging
from logging import Logger

import grpc
import communication_service_pb2_grpc
import communication_service_pb2
from communication_service_pb2 import pStatusUpdate, pFlyToDestination, pResponse, pUavStatus, pLocation3d, \
    pDirection3d, FlightState, pCapabilityData
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class MessagesClient:
    def __init__(self, logger: Logger, ip, port):
        self.logger = logger
        self.channel = grpc.insecure_channel(f'{ip}:{port}')
        self.stub = communication_service_pb2_grpc.CommunicationServiceStub(self.channel)

    def send_status_update_request(self, message_id, uav_descriptor, uav_status):
        status_update = pStatusUpdate(
            message_id=message_id,
            uav_descriptor=uav_descriptor,
            uav_status=uav_status
        )
        try:
            response = self.stub.StatusUpdateRequest(status_update)
            self.logger.debug(f"Received response: {response.response_string}")
        except grpc.RpcError as ex:
            self.logger.warning(ex)
        except Exception as ex:
            self.logger.exception('', exc_info=ex)

    def send_fly_to_destination_request(self, message_id, mission_id, is_destination_home, location):
        fly_to_destination = pFlyToDestination(
            message_id=message_id,
            mission_id=mission_id,
            is_destination_home=is_destination_home,
            location=location
        )
        try:
            response = self.stub.FlyToDestinationRequest(fly_to_destination)
            self.logger.debug(f"Received response: {response.response_string}")
        except grpc.RpcError as ex:
            self.logger.warning(ex)
        except Exception as ex:
            self.logger.exception('', exc_info=ex)

if __name__ == '__main__':
    logger1: Logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
    LoggingInitiatorByCode()

    client = MessagesClient(logger1, 'localhost', 50052)

    # Example: Sending StatusUpdate request
    client.send_status_update_request(
        message_id=1,
        uav_descriptor="UAV123",
        uav_status=pUavStatus(
            location=pLocation3d(x_lon=10, y_lat=20, h_asl=30),
            direction=pDirection3d(azimuth=45, elevation=30),
            velocity=20,
            remaining_flight_time=120,
            flight_state=FlightState.TO_DESTINATION,
            capability_data=[pCapabilityData(descriptor='JPG', data=b'12345678'),
                             pCapabilityData(descriptor='MP4', data=b'ABCDEFG')]
        )
    )

    # Example: Sending FlyToDestination request
    client.send_fly_to_destination_request(
        message_id=1,
        mission_id=10,
        is_destination_home=False,
        location=communication_service_pb2.pLocation3d(x_lon=50, y_lat=60, h_asl=40)
    )
