import grpc
from uav_communicator_pb2 import StatusUpdate, FlyToDestination, UavStatus, Location3d, Direction3d, FlightState
from uav_communicator_pb2_grpc import CommunicationServiceStub

class GroundControl:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')  # Replace with the appropriate server address

    def send_status_update(self, uav_descriptor, location, direction, velocity, remaining_flight_time, flight_state):
        status_update = StatusUpdate(
            message_id=1,
            uav_descriptor=uav_descriptor,
            uav_status=UavStatus(
                location=Location3d(x_lon=location[0], y_lat=location[1], h_asl=location[2]),
                direction=Direction3d(azimuth=direction[0], elevation=direction[1]),
                velocity=velocity,
                remaining_flight_time=remaining_flight_time,
                flight_state=flight_state
            )
        )

        stub = CommunicationServiceStub(self.channel)
        response = stub.SendStatusUpdate(status_update)
        print(f"Response from UAV: {response.response_string}")

    def send_fly_to_destination(self, uav_id, mission_id, is_destination_home, location):
        fly_to_destination = FlyToDestination(
            message_id=1,
            mission_id=mission_id,
            is_destination_home=is_destination_home,
            location=Location3d(x_lon=location[0], y_lat=location[1], h_asl=location[2])
        )

        stub = CommunicationServiceStub(self.channel)
        response = stub.SendFlyToDestination(fly_to_destination)
        print(f"Response from UAV: {response.response_string}")

if __name__ == '__main__':
    ground_control = GroundControl()

    # Example: Sending Status Update
    ground_control.send_status_update(
        uav_descriptor="UAV123",
        location=(10.0, 20.0, 30.0),
        direction=(45.0, 30.0),
        velocity=20.0,
        remaining_flight_time=120,
        flight_state=FlightState.TO_DESTINATION
    )

    # Example: Sending FlyToDestination Mission
    ground_control.send_fly_to_destination(
        uav_id="UAV123",
        mission_id=10,
        is_destination_home=False,
        location=(50.0, 60.0, 40.0)
    )
