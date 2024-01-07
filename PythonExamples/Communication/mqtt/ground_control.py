import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time

class GroundControl:
    def __init__(self, broker_address):
        self.broker_address = broker_address
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe to status topics of all drones
            client.subscribe("status/#")
        else:
            print(f"Connection failed with code {rc}")

    def on_message(self, client, userdata, msg):
        print(f"Received status update from {msg.topic}: {msg.payload.decode()}")

    def send_mission(self, drone_id, mission):
        topic = f"mission/{drone_id}"
        publish.single(topic, mission, hostname=self.broker_address)
        print(f"Sent mission to {drone_id}: {mission}")

    def start(self):
        self.client.connect(self.broker_address, 1883, 60)
        # Start the MQTT loop
        self.client.loop_forever()

# Example usage
ground_control = GroundControl("localhost")

# Send missions to drones
ground_control.send_mission("drone_1", "Waypoints: [lat1, lon1, alt1], [lat2, lon2, alt2], ...")
time.sleep(2)
ground_control.send_mission("drone_2", "Fly in a circle around a point...")
time.sleep(2)

# Start GroundControl to receive status updates
ground_control.start()
