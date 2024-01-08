# communication_server.py

import grpc
from concurrent import futures
import communication_pb2
import communication_pb2_grpc

class CommunicationService(communication_pb2_grpc.CommunicationServiceServicer):
    def SendMission(self, request, context):
        print(f"Received mission for Drone {request.drone_id}: {request.mission_data}")
        return communication_pb2.Acknowledge(message=f"Mission received for Drone {request.drone_id}")

    def SendStatusUpdate(self, request, context):
        print(f"Received status update from Drone {request.drone_id}: {request.status_message}")
        return communication_pb2.Acknowledge(message=f"Status update received from Drone {request.drone_id}")

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':

    run_server()
