import socket
import threading

class Server:
    def __init__(self, server_socket, FORMAT="utf-8", HEADER=64):
        self.server_socket = server_socket
        self.connections = []
        self.connected_addrs = set()  # NEW LINE
        self.FORMAT = FORMAT
        self.HEADER = HEADER
        self.BUFFER = 1024


    def add_connection(self, conn, addr):
        print(f"{conn} is trying to connect to the server")
        if conn in self.connections:
            print(f"{conn} is already connected...")
        else:
            self.connections.append(conn)
            print(f"New connection from {addr}, {len(self.connections)} total connections")

    def remove_connection(self, conn):
        try:
            if conn in self.connections:
                self.connections.remove(conn)
            try:
                self.connected_addrs.remove(conn.getpeername()[0])
            except KeyError:
                pass  

            try:
                conn.close()
            except Exception:
                pass 

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
                msg = conn.recv(self.BUFFER)
                if not msg:
                    break 

                msg = msg.decode(self.FORMAT)

                if msg == "!disc":
                    break  
                
                for connection in self.connections:
                    self.send_message(connection, msg)

                print(msg)

        except (ConnectionResetError, OSError) as e:
            print(f"Connection with {addr} lost: {e}")
        finally:
            self.remove_connection(conn)
