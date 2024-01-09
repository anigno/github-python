import time

import grpc
import messages_pb2
import messages_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = messages_pb2_grpc.TextMessageServiceStub(channel)

    while True:
        try:
            message = messages_pb2.TextMessage(text=f"hello from client: {time.time()}")
            response = stub.ClientSendMessage(message)
            print("Client received response:", response.text)
        except Exception as ex:
            print(ex)
        time.sleep(3)

if __name__ == '__main__':
    run()
