# communication_server.py

import grpc
from concurrent import futures
import time
import threading
import communication_pb2
import communication_pb2_grpc

class Drone:
    def __init__(self, drone_id, communication_service):
        self.drone_id = drone_id
        self.communication_service = communication_service

    def send_status_update(self, status_message):
        status_update = communication_pb2.StatusUpdate(drone_id=self.drone_id, status_message=status_message)
        response = self.communication_service.SendStatusUpdate(status_update, None)  # Pass 'None' for the context
        print(f"Status update sent from Drone {self.drone_id}: {response.text}")



def simulate_drones(communication_service):
    drone_1 = Drone(drone_id=1, communication_service=communication_service)
    drone_2 = Drone(drone_id=2, communication_service=communication_service)

    while True:
        drone_1.send_status_update(status_message="Executing mission in Area A")
        drone_2.send_status_update(status_message="Executing mission in Area B")
        time.sleep(5)

class CommunicationService(communication_pb2_grpc.CommunicationServiceServicer):
    def SendMission(self, request, context):
        print(f"Received mission for Drone {request.drone_id}: {request.mission_data}")
        return communication_pb2.Acknowledge(text=f"Mission received for Drone {request.drone_id}")

    def SendStatusUpdate(self, request, context):
        print(f"Received status update from Drone {request.drone_id}: {request.status_message}")
        return communication_pb2.Acknowledge(text=f"Status update received from Drone {request.drone_id}")

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    # Start simulating drones in a separate thread
    drone_simulation_thread = threading.Thread(target=simulate_drones, args=(CommunicationService(),))
    drone_simulation_thread.start()
    print("Server started on port 50051")

    gc=GroundControl(CommunicationService())
    gc.send_mission(1,'aaa')
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
