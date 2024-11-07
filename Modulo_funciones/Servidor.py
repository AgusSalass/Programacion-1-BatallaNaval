import socket
import json

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('192.168.104.1', 8080)

# Bind the socket to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(4)  # Allow up to 2 connections

print("Server started. Waiting for connections...")

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f"Connected by {address}")
    tengopartida = False
    # Handle the connection (e.g., send/receive data)
    conexion = True
    while conexion:
        data = connection.recv(64000).decode('utf-8')
        #if not data:
         #   conexion = False
        if data:
            partida = json.loads(data)
            print(f"Received: {data}")
            print(partida["turno"])
            data = json.dumps(partida)
            connection.sendall(data.encode('utf-8'))
    print("cerre")