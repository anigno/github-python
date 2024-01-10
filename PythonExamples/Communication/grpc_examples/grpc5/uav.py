import grpc
from concurrent import futures
import time
import communication_pb2
import communication_pb2_grpc

class Uav(communication_pb2_grpc.CommunicationServiceServicer):
    def SendMission(self, request, context):
        print(f"UAV received mission: {request.mission_data}")

        # Process the mission and generate an acknowledgment
        acknowledge = communication_pb2.Acknowledge(message="Mission received and in progress")
        return acknowledge

    def SendStatus(self, request, context):
        print(f"UAV received status: Latitude {request.latitude}, Longitude {request.longitude}, State: {request.state}")

        # Process the status and generate an acknowledgment
        acknowledge = communication_pb2.Acknowledge(message="Status received and acknowledged")
        return acknowledge

def run_uav_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServiceServicer_to_server(Uav(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("UAV server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    run_uav_server()
