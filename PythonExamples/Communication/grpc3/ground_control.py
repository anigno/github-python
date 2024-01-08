# communication_client.py
import time

import grpc
import communication_pb2
import communication_pb2_grpc

class GroundControl:
    def __init__(self, stub):
        self.stub = stub

    def send_mission(self, drone_id, mission_data):
        mission = communication_pb2.Mission(drone_id=drone_id, mission_data=mission_data)
        response = self.stub.SendMission(mission)
        print(f"Mission sent to Drone {drone_id}: {response.text}")

    def receive_status_update(self, drone_id, status_message):
        status_update = communication_pb2.StatusUpdate(drone_id=drone_id, status_message=status_message)
        response = self.stub.SendStatusUpdate(status_update)
        print(f"Status update received from Drone {drone_id}: {response.text}")

def run_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = communication_pb2_grpc.CommunicationServiceStub(channel)
        ground_control = GroundControl(stub)

        while True:
            try:
                ground_control.send_mission(drone_id=1, mission_data="Explore Area A")
                ground_control.send_mission(drone_id=2, mission_data="Inspect Area B")
            except Exception as ex:
                print('error sending mission',ex)
            time.sleep(3)
            # Periodically sending status updates from Drones to GroundControl
            ground_control.receive_status_update(drone_id=1, status_message="Executing mission in Area A")
            ground_control.receive_status_update(drone_id=2, status_message="Executing mission in Area B")
            time.sleep(3)


if __name__ == '__main__':
    run_client()
