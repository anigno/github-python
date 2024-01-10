from threading import Thread

import grpc
from concurrent import futures
import time
import messages_pb2
import messages_pb2_grpc

class TextMessageReceivingService(messages_pb2_grpc.TextMessageServiceServicer):
    def ClientSendMessage(self, request, context):
        print(f'server received: {request.text}')
        response = messages_pb2.ResponseMessage()
        response.text = "Server ack for: " + request.text
        return response

class GrpcServer:
    def __init__(self):
        self.server_thread = Thread(target=self.server_thread_start(), daemon=True)

    def server_thread_start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        messages_pb2_grpc.add_TextMessageServiceServicer_to_server(TextMessageReceivingService(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()

    def start(self):
        self.server_thread.start()

if __name__ == '__main__':
    grpc_server = GrpcServer()
    grpc_server.start()
