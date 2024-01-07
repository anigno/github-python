import paho.mqtt.client as mqtt
import time

class Drone:
    def __init__(self, drone_id, broker_address):
        self.drone_id = drone_id
        self.broker_address = broker_address
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def on_message(self, client, userdata, msg):
        print(f"Received mission for {msg.topic}: {msg.payload.decode()}")
        # Process the mission (example: simulate mission execution)
        time.sleep(3)  # Simulate processing time
        # Send status update back to GroundControl
        self.send_status_update(f"Mission completed: {msg.payload.decode()}")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe to the mission topic for this drone
            client.subscribe(f"mission/{self.drone_id}")
        else:
            print(f"Connection failed with code {rc}")

    def on_disconnect(self, client, userdata, rc):
        print(f"Disconnected with result code {rc}")
        # Implement your reconnection logic here
        while not client.is_connected():
            print("Attempting to reconnect...")
            try:
                client.reconnect()
            except Exception as e:
                print(f"Reconnection failed: {e}")
                time.sleep(5)  # Wait for a while before retrying

    def send_status_update(self, status):
        topic = f"status/{self.drone_id}"
        self.client.publish(topic, status)

    def start(self):
        self.client.connect(self.broker_address, 1883, 60)
        # Start the MQTT loop
        self.client.loop_start()

        # Example: Periodically send status updates
        while True:
            status_message = f"Status update from {self.drone_id}: {time.ctime()}"
            self.send_status_update(status_message)
            time.sleep(5)  # Send status update every 5 seconds

# Example usage
drone = Drone("drone_1", "localhost")
drone.start()
