import grpc
from communication_service_pb2_grpc import CommunicationServiceStub
from communication_service_pb2 import DroneUpdate, Mission

def send_mission(drone_id, mission_data):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CommunicationServiceStub(channel)
        mission = Mission(drone_id=drone_id, mission_data=mission_data)
        stub.SendMission(mission)

# Assume a function to handle drone updates
def handle_drone_update(update):
    print(f"Received update from {update.drone_id}")

# Set up streaming from drones
def drone_update_stream():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CommunicationServiceStub(channel)
        for update in stub.SendDroneUpdate(iter([DroneUpdate(drone_id='123'), DroneUpdate(drone_id='456')])):
            handle_drone_update(update)

if __name__ == "__main__":
    # Send mission to a specific drone
    send_mission(drone_id='123', mission_data='Fly to coordinates (x, y)')

    # Receive continuous updates from all drones
    drone_update_stream()
