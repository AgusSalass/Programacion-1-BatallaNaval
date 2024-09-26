import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('192.168.191.5', 8080)

# Bind the socket to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)  # Allow up to 2 connections

print("Server started. Waiting for connections...")

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f"Connected by {address}")

    # Handle the connection (e.g., send/receive data)
    conexion = True
    while conexion:
        data = connection.recv(1024)
        if not data:
            conexion = False
        print(f"Received: {data.decode()}")
        connection.sendall(data)

    # Close the connection
    connection.close()