# drone_client.py
import grpc
from uav_communicator_pb2 import StatusUpdate, FlyToDestination
from uav_communicator_pb2_grpc import CommunicationServiceStub

# drone_client.py
import grpc
import time


def send_status_update(uav_descriptor, location, direction, velocity, remaining_flight_time, flight_state):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CommunicationServiceStub(channel)
        status_update_request = StatusUpdate(
            message_id=1,
            uav_descriptor=uav_descriptor,
            uav_status={
                'location': {
                    'x_lon': location[0],
                    'y_lat': location[1],
                    'h_asl': location[2],
                },
                'direction': {
                    'azimuth': direction[0],
                    'elevation': direction[1],
                },
                'velocity': velocity,
                'remaining_flight_time': remaining_flight_time,
                'flight_state': flight_state,
            }
        )
        response = stub.SendStatusUpdate(status_update_request)
        print(f"StatusUpdate response: {response.response_string}")

def receive_fly_to_destination():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CommunicationServiceStub(channel)
        for fly_to_destination_response in stub.SendFlyToDestination(None):
            print(f"Received FlyToDestination message for mission {fly_to_destination_response.mission_id}")
            # Process the fly to destination response as needed

if __name__ == '__main__':
    drone_descriptor = "Drone001"
    drone_location = (37.7749, -122.4194, 100)  # Example location (lat, lon, altitude)
    drone_direction = (45.0, 30.0)  # Example direction (azimuth, elevation)
    drone_velocity = 10.0
    drone_remaining_flight_time = 120
    drone_flight_state = 20  # Example FlightState.TO_DESTINATION

    while True:
        send_status_update(drone_descriptor, drone_location, drone_direction,
                            drone_velocity, drone_remaining_flight_time, drone_flight_state)
        time.sleep(5)  # Send status update every 5 seconds
        receive_fly_to_destination()
