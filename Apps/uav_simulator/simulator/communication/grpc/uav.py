import grpc
from concurrent import futures
from uav_communicator_pb2 import UavStatus, FlyToDestination, response
from uav_communicator_pb2_grpc import CommunicationServiceServicer, add_CommunicationServiceServicer_to_server

class Uav(CommunicationServiceServicer):
    def __init__(self, uav_id):
        self.uav_id = uav_id
        self.uav_status = UavStatus()  # Initialize with default values

    def SendStatusUpdate(self, request, context):
        self.uav_status = request.uav_status
        print(f"Received status update from GroundControl for UAV {self.uav_id}")
        return response(response_string=f"Status update received for UAV {self.uav_id}")

    def SendFlyToDestination(self, request, context):
        print(f"Received FlyToDestination mission for UAV {self.uav_id}: {request}")
        # Implement logic to handle the mission, e.g., update location
        return response(response_string=f"FlyToDestination mission received for UAV {self.uav_id}")

def serve(uav_id):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    uav_instance = Uav(uav_id)
    add_CommunicationServiceServicer_to_server(uav_instance, server)
    server.add_insecure_port('[::]:50051')
    print(f"Starting UAV server for UAV {uav_id} on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    uav_id = input("Enter UAV ID: ")
    serve(uav_id)
