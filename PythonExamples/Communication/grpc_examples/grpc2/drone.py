import grpc
import communication_pb2
import communication_pb2_grpc
import time

class DroneClient:
    def __init__(self, drone_id):
        self.drone_id = drone_id
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = communication_pb2_grpc.CommunicationServiceStub(self.channel)

    def send_mission(self, mission_data):
        mission = communication_pb2.Mission(drone_id=self.drone_id, mission_data=mission_data)
        response = None
        retry_count = 0

        while retry_count < 3:  # Retry up to 3 times
            try:
                response = self.stub.SendMission(mission)
                print(f"Received response for mission: {response.status_message}")
                break  # Break the loop if successful
            except grpc.RpcError as e:
                print(f"Error sending mission: {e}")
                retry_count += 1
                time.sleep(2**retry_count)  # Exponential backoff

        return response

    def send_status_update(self, status_message):
        status_update = communication_pb2.StatusUpdate(drone_id=self.drone_id, status_message=status_message)
        response = self.stub.SendStatusUpdate(status_update)
        print(f"Received response for status update: {response.status_message}")

if __name__ == '__main__':
    drone_1 = DroneClient("drone_1")

    # Send missions to drones
    drone_1.send_mission("Waypoints: [lat1, lon1, alt1], [lat2, lon2, alt2], ...")
    time.sleep(2)

    # Simulate disconnection and reconnection
    print("Simulating disconnection...")
    time.sleep(5)
    print("Simulating reconnection...")

    # Send missions again after reconnection
    drone_1.send_mission("Fly in a circle around a point...")
    time.sleep(2)

    # Periodically send status updates
    while True:
        drone_1.send_status_update(f"Status update from drone_1: {time.ctime()}")
        time.sleep(5)
