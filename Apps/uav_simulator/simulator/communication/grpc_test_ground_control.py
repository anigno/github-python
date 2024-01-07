# ground_control_service.py
from threading import Thread

import grpc
from concurrent import futures
import time
from uav_communicator_pb2 import StatusUpdate, FlyToDestination, response
from uav_communicator_pb2_grpc import CommunicationServiceServicer, add_CommunicationServiceServicer_to_server
from uav_communicator_pb2_grpc import CommunicationServiceStub
# ground_control_service.py
import grpc
from concurrent import futures
import time

class CommunicationServicer(CommunicationServiceServicer):
    def SendStatusUpdate(self, request, context):
        print(f"Received StatusUpdate message from UAV: {request.uav_descriptor}")
        # Process the status update and generate a response if needed
        return response(response_string="Status update received successfully")

    def SendFlyToDestination(self, request, context):
        print(f"Received FlyToDestination message for mission {request.mission_id}")
        # Process the fly to destination request and generate a response if needed
        return response(response_string="FlyToDestination request received successfully")

    def SendFlyToDestinationGenerator(self, request, context):
        # This is a server streaming RPC method
        # You can implement logic to send FlyToDestination messages based on received status updates
        for _ in range(5):  # Send 5 sample FlyToDestination messages
            yield FlyToDestination(
                message_id=2,
                mission_id=123,
                is_destination_home=False,
                location={'x_lon': 35.0, 'y_lat': -120.0, 'h_asl': 50.0}  # Example destination location
            )
            time.sleep(10)  # Wait for 10 seconds between each FlyToDestination message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CommunicationServiceServicer_to_server(CommunicationServicer(), server)
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
