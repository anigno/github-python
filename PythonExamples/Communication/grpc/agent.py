import grpc
from concurrent import futures
import communicator_pb2
import communicator_pb2_grpc

class CommunicatorServicer(communicator_pb2_grpc.CommunicatorServicer):
    def SendMessage(self, request, context):
        # Process incoming message
        processed_message = process_message(request.content)
        return communicator_pb2.Message(content=processed_message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communicator_pb2_grpc.add_CommunicatorServicer_to_server(CommunicatorServicer(), server)
    server.add_insecure_port("[::]:50051")  # Or use a secure port
    server.start()
    server.wait_for_termination()

def send_message(message):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = communicator_pb2_grpc.CommunicatorStub(channel)
        response = stub.SendMessage(communicator_pb2.Message(content=message))
        return response.content

def process_message(message):
    # Perform calculations or processing based on message type
    if message.type == "calculation":
        result = calculate_something(message.content)
        return result
    else:
        return "Message received: " + message.content

# Start the server
serve()

# Send a message and receive a response
response = send_message("Hello from app1")
print("Received response:", response)

