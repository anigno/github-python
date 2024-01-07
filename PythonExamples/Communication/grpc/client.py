import grpc
import messages_pb2
import messages_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = messages_pb2_grpc.TextMessageServiceStub(channel)
    message = messages_pb2.TextMessage(text="Hello, gRPC!")

    response = stub.SendMessage(message)
    print("Client received:", response.text)

if __name__ == '__main__':
    run()
