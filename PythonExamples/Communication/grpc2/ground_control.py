import grpc
from concurrent import futures
import time

import communication_pb2
import communication_pb2_grpc

class CommunicationServicer(communication_pb2_grpc.CommunicationServiceServicer):
    def SendMission(self, request, context):
        print(f"Received mission for {request.drone_id}: {request.mission_data}")
        # Process the mission (simulate processing time)
        time.sleep(3)
        return communication_pb2.StatusUpdate(drone_id=request.drone_id, status_message="Mission completed")

    def SendStatusUpdate(self, request, context):
        print(f"Received status update from {request.drone_id}: {request.status_message}")
        return communication_pb2.StatusUpdate(drone_id=request.drone_id, status_message="Status update received")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051")
    try:
        while True:
            time.sleep(86400)  # One day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
