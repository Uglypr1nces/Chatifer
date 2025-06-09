import socket

class Server:
    def __init__(self, server_socket, FORMAT, HEADER):
        self.server_socket = server_socket
        self.connections = []
        self.usernames = []
        self.FORMAT = FORMAT
        self.HEADER = HEADER

    def add_connection(self, conn, addr):
        self.connections.append(conn)
        print(f"New connection from {addr}, {len(self.connections)} amount of connections")
        message = f"afXMZhjvchs88vjls.g87satv0q,.7fgy{len(self.connections)}"
        for connection in self.connections:
            self.send_message(connection, message)
  
    def remove_connection(self, conn):
        try:
            index = self.connections.index(conn)
            self.connections.remove(index)
            username = self.usernames.pop(index)
            self.usernames.remove(index)
            for connection in self.connections:
                self.send_message(connection, f"{username} has left the chat.")
            conn.close()
            print(f"Connection with {addr} closed.")
        except:
            print("Error removing connection")

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
                msg = conn.recv(1024).decode(self.FORMAT)
                if not msg:
                    print(f"Connection with {addr} closed.")
                    try:
                        self.remove_connection(conn)
                    except:
                        print("Error removing connection")
                    break

                if msg == "!disc":
                    conn.close()
                    self.remove_connection(conn)
                    print(f"Connection with {addr} closed.")
                    break
                

                print(msg)

        except ConnectionResetError:
            print(f"Connection with {addr} was forcibly closed.")
        finally:
            conn.close()


