import socket
import json
import threading
import Core as f
import os

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
    path_tableros = os.path.dirname(os.path.abspath(__file__))
    arch_tab = os.path.join(path_tableros, f"Tableros.json")
    global partida
    while True:
        try:
            # Recibir datos del cliente
            mensajeCompleto=False
            data=""
            while not mensajeCompleto:
                data = data + connection.recv(1048576).decode('utf-8')
                if data.endswith("FinDeMensaje"):
                    data=data[0:len(data)-12]
                    mensajeCompleto=True
            if data:
                # Actualizar el diccionario con los datos recibidos
                new_data = json.loads(data)
                partida = ({"Jugador 1": new_data[0], "Jugador 2": new_data[1], "Datos": new_data[2]})
                if partida["Datos"]["turno"] == 1:
                    partida["Datos"]["turno"] = 2
                elif partida["Datos"]["turno"] == 2:
                    partida["Datos"]["turno"] = 1
                #partida.update(new_data)
                print(f'Data received and updated: {partida}')

                # Enviar el diccionario actualizado a todos los clientes
                mensaje = json.dumps((partida["Jugador 1"], partida["Jugador 2"], partida["Datos"]))
                contenido = open(arch_tab, "w")
                contenido.write(mensaje)
                contenido.close()
                broadcast(mensaje.encode('utf-8'))
        except Exception as e:
            print(f'Error: {e}')

        #connection.close()
        #clients.remove(connection)

def broadcast(message):
    message=message+"FinDeMensaje"
    for client in clients:
        try:
            client.sendall(message)
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