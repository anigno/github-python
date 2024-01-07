import grpc
from concurrent import futures
import time
import messages_pb2
import messages_pb2_grpc

class TextMessageService(messages_pb2_grpc.TextMessageServiceServicer):
    def SendMessage(self, request, context):
        response = messages_pb2.TextMessage()
        response.text = "Server received: " + request.text
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_TextMessageServiceServicer_to_server(TextMessageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
