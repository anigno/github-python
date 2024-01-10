from PythonExamples.Communication.grpc3 import communication_pb2_grpc, communication_pb2

class CommunicationService(communication_pb2_grpc.CommunicationServiceServicer):
    def SendMission(self, request, context):
        print(f"send mission {request.drone_id}: {request.mission_data}")
        return communication_pb2.Acknowledge(text=f"mission to {request.drone_id}")

    def SendStatusUpdate(self, request, context):
        print(f"Received status update from Drone {request.drone_id}: {request.status_message}")
        return communication_pb2.Acknowledge(text=f"Status update received from Drone {request.drone_id}")
