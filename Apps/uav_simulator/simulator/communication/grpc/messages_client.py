import grpc
import communication_service_pb2_grpc
import communication_service_pb2

class MessagesClient:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = communication_service_pb2_grpc.CommunicationServiceStub(self.channel)

    def send_status_update_request(self, message_id, uav_descriptor, uav_status):
        status_update = communication_service_pb2.pStatusUpdate(
            message_id=message_id,
            uav_descriptor=uav_descriptor,
            uav_status=uav_status
        )
        response = self.stub.StatusUpdateRequest(status_update)
        print(f"Received response: {response.response_string}")

    def send_fly_to_destination_request(self, message_id, mission_id, is_destination_home, location):
        fly_to_destination = communication_service_pb2.pFlyToDestination(
            message_id=message_id,
            mission_id=mission_id,
            is_destination_home=is_destination_home,
            location=location
        )
        response = self.stub.FlyToDestinationRequest(fly_to_destination)
        print(f"Received response: {response.response_string}")

if __name__ == '__main__':
    client = MessagesClient('localhost:50051')

    # Example: Sending StatusUpdate request
    client.send_status_update_request(
        message_id=1,
        uav_descriptor="UAV123",
        uav_status=communication_service_pb2.pUavStatus(
            location=communication_service_pb2.pLocation3d(x_lon=10, y_lat=20, h_asl=30),
            direction=communication_service_pb2.pDirection3d(azimuth=45, elevation=30),
            velocity=20,
            remaining_flight_time=120,
            flight_state=communication_service_pb2.FlightState.TO_DESTINATION
        )
    )

    # Example: Sending FlyToDestination request
    client.send_fly_to_destination_request(
        message_id=1,
        mission_id=10,
        is_destination_home=False,
        location=communication_service_pb2.pLocation3d(x_lon=50, y_lat=60, h_asl=40)
    )
