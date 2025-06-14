import socket
from threading import Thread
from queue import Queue

class ChatClient:
    def __init__(self):
        self.HEADER = 64
        self.FORMAT = "utf-8"
        self.ADDR = None
        self.client = None
        self.message_queue = Queue()
        self.running = False

    def set_server(self, server, port):
        self.ADDR = (server, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server set to", server, "on port", port)

    def connect(self):
        if self.ADDR:
            self.client.connect(self.ADDR)
            print("Connected to", self.ADDR)

    def disconnect(self):
        self.running = False
        try:
            self.send_message("!disc")
        except:
            pass
        self.client.close()
        print("Disconnected from", self.ADDR)
        self.ADDR = None

    def listen(self):
        self.running = True
        while self.running:
            try:
                msg_length = self.client.recv(self.HEADER).decode(self.FORMAT).strip()
                if msg_length:
                    msg_length = int(msg_length)
                    msg = self._recv_exact(msg_length).decode(self.FORMAT)
                    self.message_queue.put(msg)
            except:
                break

    def _recv_exact(self, n):
        data = b''
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                break
            data += packet
        return data

    def send_message(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def get_latest_message(self):
        if not self.message_queue.empty():
            return self.message_queue.get()
        return None


user_client = ChatClient()
