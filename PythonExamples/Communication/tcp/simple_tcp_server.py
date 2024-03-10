import socket

# Server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9999

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming connections (max backlog of 5 connections)
server_socket.listen(5)

print(f"Server listening on {SERVER_ADDRESS}:{SERVER_PORT}...")

while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        if data:
            # Echo back the received data
            print(f"Received: {data.decode()}")
            client_socket.sendall(data)
        else:
            print("No data received from client.")

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        # Close the client socket
        client_socket.close()
