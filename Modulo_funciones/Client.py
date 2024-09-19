import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('10.100.51.252', 12345)

# Connect to the server
client_socket.connect(server_address)

print("Connected to the server.")

# Send data to the server
client_socket.sendall(b"Hello, server!")

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Close the connection
client_socket.close()