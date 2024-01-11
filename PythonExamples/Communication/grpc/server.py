import math
import grpc
from concurrent import futures
import calculation_service_pb2
import calculation_service_pb2_grpc

class CalculationService(calculation_service_pb2_grpc.CalculateServiceServicer):
    """the service class definition, all service methods should be implemented here"""

    def calculate_square_root(self, request, context):
        """server method to serve client square root requests and return a response message"""
        print(f'server received: {request.sender_id} {request.number}')
        response = calculation_service_pb2.ResponseMessage()
        response.result = math.sqrt(request.number)
        return response

class GrpcServer:
    def start(self):
        # use thread pool to serve multiple requests
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        calculation_service_pb2_grpc.add_CalculateServiceServicer_to_server(CalculationService(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()

if __name__ == '__main__':
    GrpcServer().start()
