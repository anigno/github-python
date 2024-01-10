import time
from threading import Thread

import grpc
import messages_pb2
import messages_pb2_grpc

class GrpcClient:
    def __init__(self, id):
        print(f'drone {id}')
        self.id = id
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = messages_pb2_grpc.TextMessageServiceStub(channel)
        self.client_thread = Thread(target=self.client_thread_start(), daemon=False)

    def client_thread_start(self):
        while True:
            try:
                message = messages_pb2.TextMessage(text=f"hello from client {self.id}: {time.time()}")
                response = self.stub.ClientSendMessage(message)
                print("Client received response:", response.text)
            except Exception as ex:
                print(ex)
            time.sleep(3)

    # def start(self):
    #     self.client_thread.start()

if __name__ == '__main__':
    d1 = GrpcClient(1)
    d2 = GrpcClient(2)

