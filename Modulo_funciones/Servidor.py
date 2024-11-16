import socket
import json
import threading
import Core as f

partida = {}

clients = []

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('192.168.191.52', 8080)

# Bind the socket to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(4)  # Allow up to 2 connections

print("Server started. Waiting for connections...")

def handle_client(connection):
    global partida
    while True:
        try:
            # Recibir datos del cliente
            data = connection.recv(1048576).decode('utf-8')
            if data:
                # Actualizar el diccionario con los datos recibidos
                new_data = json.loads(data)
                partida.update(new_data)
                print(f'Data received and updated: {partida}')

                # Enviar el diccionario actualizado a todos los clientes
                mensaje = json.dumps(partida).encode('utf-8')
                broadcast(mensaje)
        except Exception as e:
            print(f'Error: {e}')

        #connection.close()
        #clients.remove(connection)

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            clients.remove(client)

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f"Connected by {address}")
    clients.append(connection)
    thread = threading.Thread(target=handle_client, args=(connection,))
    thread.start()    