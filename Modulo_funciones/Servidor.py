import socket
import json
import threading
import Core as f
import os

partida = {}

clients = []

'''Crea un objeto socket'''
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''define la direccion y el puerto del server'''
server_address = ('192.168.60.114', 8080)

'''enlaza el socket a la direccion y el puerto'''
server_socket.bind(server_address)

'''escucha las conexiones entrantes, permite hasta 2 conexiones'''
server_socket.listen(2)

print("Server started. Waiting for connections...")

def handle_client(connection):
    global partida
    while True:
        try:
            '''Recibe los datos del cliente'''
            mensajeCompleto=False
            data=""
            while not mensajeCompleto:
                data = data + connection.recv(1048576).decode('utf-8')
                if data.endswith("FinDeMensaje"):
                    data=data[0:len(data)-12]
                    mensajeCompleto=True
            if data:
                '''Actualiza el diccionario con los datos recibidos'''
                new_data = json.loads(data)
                partida = ({"Jugador 1": new_data[0], "Jugador 2": new_data[1], "Datos": new_data[2]})
                if partida["Datos"]["turno"] == 1:
                    partida["Datos"]["turno"] = 2
                elif partida["Datos"]["turno"] == 2:
                    partida["Datos"]["turno"] = 1
                print(f'Data received and updated: {partida}')

                '''Envio del diccionario actualizado a todos los clientes'''
                mensaje = json.dumps((partida["Jugador 1"], partida["Jugador 2"], partida["Datos"]))
                broadcast(mensaje)
        except Exception as e:
            print(f'Error: {e}')

def broadcast(message):
    message=message+"FinDeMensaje"
    for client in clients:
        try:
            client.sendall(message.encode('utf-8'))
        except:
            client.close()
            clients.remove(client)

while True:
    '''acepta la conexion entrante y la enlaza a un hilo'''
    connection, address = server_socket.accept()
    print(f"Connected by {address}")
    clients.append(connection)
    thread = threading.Thread(target=handle_client, args=(connection,))
    thread.start()    