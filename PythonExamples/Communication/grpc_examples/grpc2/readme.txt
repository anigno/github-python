In this example:

The DroneClient class includes a simple retry mechanism for sending missions, and it will automatically attempt to
reconnect and resend the mission if a disconnection occurs.
The GroundControl (gRPC server) is running on port 50051.
The DroneClient (gRPC client) connects to the server, sends missions, and periodically sends status updates.
You can run multiple instances of the DroneClient with different drone IDs to simulate multiple drones.
The disconnect/reconnect logic is integrated into the send_mission method.
You can extend this logic to other RPC calls as needed.



pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. communication.proto
