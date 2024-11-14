import socket
import json
import threading

def send_data(client_socket):
    while True:
        # Cargar datos en el diccionario
        key = input("Ingrese la clave: ")
        value = input("Ingrese el valor: ")
        data = {key: value}
        
        # Enviar el diccionario al servidor
        client_socket.send(json.dumps(data).encode('utf-8'))

def receive_data(client_socket):
    while True:
        try:
            # Recibir datos del servidor
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                break
            print(f'Dictionary updated by server: {data}')
        except:
            print("Error en la recepciÃ³n de datos.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.104.114', 12345))

    # Crear hilos para enviar y recibir datos
    thread_send = threading.Thread(target=send_data, args=(client_socket,))
    thread_receive = threading.Thread(target=receive_data, args=(client_socket,))
    
    thread_send.start()
    thread_receive.start()

if __name__ == "__main__":
    start_client()