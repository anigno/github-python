import time

import grpc
from concurrent import futures
from threading import Thread
import communication_pb2
import communication_pb2_grpc
from PythonExamples.Communication.grpc3.communication_service import CommunicationService

class GroundControl:
    def __init__(self, communication_service):
        self.communication_service = communication_service

    def send_mission(self, drone_id, mission_data):
        mission = communication_pb2.Mission(drone_id=drone_id, mission_data=mission_data)
        response = self.communication_service.SendMission(mission, None)  # Pass 'None' for the context
        print(f"Mission sent to Drone {drone_id}: {response.text}")

    def thread_start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        communication_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationService(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()

    def start(self):
        Thread(target=self.thread_start, daemon=True)

if __name__ == '__main__':
    gc = GroundControl(CommunicationService())
    while True:
        try:
            gc.send_mission(1, 'aaa')
        except Exception as ex:
            print(ex)
        time.sleep(3)
