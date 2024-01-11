import grpc
from communication_service_pb2_grpc import CommunicationServiceStub
from communication_service_pb2 import DroneUpdate, Mission

def send_drone_update():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CommunicationServiceStub(channel)
        updates = iter([DroneUpdate(drone_id='123', update_data='Some data'), DroneUpdate(drone_id='456', update_data='Another data')])
        stub.SendDroneUpdate(updates)

if __name__ == "__main__":
    # Send continuous updates to the ground system
    send_drone_update()
