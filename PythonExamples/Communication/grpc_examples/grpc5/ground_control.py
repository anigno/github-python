# communication_client.py

import grpc
import communication_pb2
import communication_pb2_grpc

class GroundControl:
    def send_mission(self, stub, mission_data):
        mission = communication_pb2.Mission(mission_data=mission_data)
        acknowledge = stub.SendMission(mission)
        print(f"Ground Control received acknowledgment: {acknowledge.message}")

    def send_status(self, stub, latitude, longitude, state):
        status = communication_pb2.Status(
            latitude=latitude,
            longitude=longitude,
            state=state
        )
        acknowledge = stub.SendStatus(status)
        print(f"Ground Control received acknowledgment: {acknowledge.message}")

def run_ground_control_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = communication_pb2_grpc.CommunicationServiceStub(channel)

        ground_control = GroundControl()

        # Ground Control sends a mission to UAV
        ground_control.send_mission(stub, "Explore Area A")

        # Ground Control sends a status to UAV
        ground_control.send_status(stub, "37.7749", "-122.4194", "Waiting for instructions")

if __name__ == '__main__':
    run_ground_control_client()
