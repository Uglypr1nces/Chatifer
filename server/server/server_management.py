import socket
import threading

class Server:
    def __init__(self, server_socket, FORMAT="utf-8", HEADER=64):
        self.server_socket = server_socket
        self.connections = []
        self.FORMAT = FORMAT
        self.HEADER = HEADER
        self.BUFFER = 1024

    def add_connection(self, conn, addr):
        self.connections.append(conn)
        print(f"New connection from {addr}, {len(self.connections)} total connections")

    def remove_connection(self, conn):
        try:
            index = self.connections.index(conn)
            self.connections.pop(index)
            conn.close()
            print(f"Connection with {conn.getpeername()} closed.")
        except Exception as e:
            print(f"Error removing connection: {e}")

    def send_message(self, conn, msg):
        try:
            message = msg.encode(self.FORMAT)
            conn.send(message)
        except Exception as e:
            print(f"Error sending message: {e}")
            self.remove_connection(conn)

    def handle_client(self, conn, addr):
        try:
            while True:
                msg = conn.recv(self.BUFFER).decode(self.FORMAT)

                if msg == "!disc":
                    self.remove_connection(conn)
                    break

                for connection in self.connections:
                     self.send_message(connection, msg)

                print(msg)

        except ConnectionResetError:
            print(f"Connection with {addr} was forcibly closed.")
        finally:
            self.remove_connection(conn)
