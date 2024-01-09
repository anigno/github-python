import grpc
from concurrent import futures
import time
import threading
import communication_pb2
import communication_pb2_grpc

class GroundControl:
    def __init__(self, communication_service):
        self.communication_service = communication_service

    def send_mission(self, drone_id, mission_data):
        mission = communication_pb2.Mission(drone_id=drone_id, mission_data=mission_data)
        response = self.communication_service.SendMission(mission, None)  # Pass 'None' for the context
        print(f"Mission sent to Drone {drone_id}: {response.text}")

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
    return server

if __name__ == '__main__':
    server1 = run_server()
    gc = GroundControl(CommunicationService())
    gc.send_mission(1, 'aaa')

    server1.wait_for_termination()
