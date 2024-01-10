import grpc
from concurrent import futures
import time
import threading
import communication_pb2
import communication_pb2_grpc

class Drone:
    def __init__(self, drone_id, communication_service):
        self.drone_id = drone_id
        self.communication_service = communication_service

    def send_status_update(self, status_message):
        status_update = communication_pb2.StatusUpdate(drone_id=self.drone_id, status_message=status_message)
        response = self.communication_service.SendStatusUpdate(status_update, None)  # Pass 'None' for the context
        print(f"Status update sent from Drone {self.drone_id}: {response.text}")

if __name__ == '__main__':
    drone_1 = Drone(drone_id=1, communication_service=communication_pb2_grpc.CommunicationService())
    while True:
        try:
            drone_1.send_status_update(status_message="Executing mission in Area A")
        except Exception as ex:
            print(ex)
        time.sleep(3)
