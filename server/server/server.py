import socket
import threading
from server_management import Server

port = 9246
server = "localhost"
HEADER = 64
ADDR = (server, port)
FORMAT = "utf-8"

# Creating a socket, picking the family, pick a type
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

server_manager = Server(server_socket,FORMAT,HEADER)

def start(): 
    server_socket.listen()
    print(f"SERVER STARTING AT {server}, {port}...")
    while True:
        conn, addr = server_socket.accept()  # Waits for a connection, when a connection occurs it will store the data
        server_manager.add_connection(conn, addr)
        thread = threading.Thread(target=server_manager.handle_client, args=(conn, addr))
        thread.start()
