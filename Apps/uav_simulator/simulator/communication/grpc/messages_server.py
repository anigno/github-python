import grpc
from concurrent import futures

from Apps.uav_simulator.simulator.communication.grpc import communication_service_pb2_grpc
from communication_service_pb2 import pStatusUpdate, pFlyToDestination, pResponse
from communication_service_pb2_grpc import CommunicationServiceServicer, add_CommunicationServiceServicer_to_server

class MessagesServer(CommunicationServiceServicer):
    def StatusUpdateRequest(self, request, context):
        # Implement your logic to handle StatusUpdate requests
        print(f"Received StatusUpdate request: {request}")
        response = pResponse(response_string="StatusUpdate request received")
        return response

    def FlyToDestinationRequest(self, request, context):
        # Implement your logic to handle FlyToDestination requests
        print(f"Received FlyToDestination request: {request}")
        response = pResponse(response_string="FlyToDestination request received")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_service_pb2_grpc.add_CommunicationServiceServicer_to_server(MessagesServer(), server)
    server.add_insecure_port('[::]:50051')
    print("Communication Service Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
