import random
import time
from threading import Thread

import grpc
import calculation_service_pb2
import calculation_service_pb2_grpc

class GrpcClient:
    def __init__(self, sender_id):
        self.sender_id = sender_id
        self.client_thread = Thread(target=self.client_thread_start, daemon=False)
        # create channel and stab for using the service
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = calculation_service_pb2_grpc.CalculateServiceStub(channel)

    def client_thread_start(self):
        rnd = random.Random()
        for a in range(100, 200):
            # creating a request message, send it and get a response from server
            message = calculation_service_pb2.RequestMessage(sender_id=self.sender_id, number=a)
            response = self.stub.calculate_square_root(message)
            print("Client received response:", response.result)
            time.sleep(rnd.randint(100, 200) / 1000)

    def start(self):
        self.client_thread.start()

if __name__ == '__main__':
    GrpcClient('client A').start()
    GrpcClient('client B').start()
    GrpcClient('client C').start()
    GrpcClient('client D').start()
    GrpcClient('client E').start()
    GrpcClient('client F').start()
