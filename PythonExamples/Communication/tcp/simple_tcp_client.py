import socket

# Server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9999

# Message to send
message = 'Hello, TCP Server!'

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f'Received from server: {response.decode()}')

except ConnectionRefusedError:
    print('Connection was refused.')