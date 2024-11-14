import socket
import threading
import json

# Diccionario compartido
data_dict = {}

# Lista para mantener la conexiÃ³n de los clientes
clients = []

def handle_client(client_socket):
    global data_dict
    while True:
        try:
            # Recibir datos del cliente
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            
            # Actualizar el diccionario con los datos recibidos
            new_data = json.loads(data)
            data_dict.update(new_data)
            print(f'Data received and updated: {data_dict}')

            # Enviar el diccionario actualizado a todos los clientes
            broadcast(json.dumps(data_dict).encode('utf-8'))
        except Exception as e:
            print(f'Error: {e}')
            break
    
    client_socket.close()
    clients.remove(client_socket)

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)  # Escuchar hasta 2 clientes
    print('Server is listening...')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Client connected: {addr}')
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()