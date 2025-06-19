import requests
from queue import Queue

class ChatHttpClient:
    def __init__(self):
        self.server_url = None
        self.message_queue = Queue()
        self.session = requests.Session()

    def set_server(self, server_url):
        self.server_url = server_url
        print("Server set to", server_url)

    def connect(self):
        if self.server_url:
            response = self.session.post(f"{self.server_url}/connect")
            print("Connected:", response.text)

    def disconnect(self):
        if self.server_url:
            try:
                self.send_message("!disc")
            except:
                pass
            self.session.post(f"{self.server_url}/disconnect")
            print("Disconnected from", self.server_url)
            self.server_url = None

    def listen(self):
        # This is a polling simulation — not real-time like sockets
        import time
        while self.server_url:
            try:
                response = self.session.get(f"{self.server_url}/latest-message")
                if response.status_code == 200 and response.text:
                    self.message_queue.put(response.text)
            except:
                break
            time.sleep(1)  # Poll every second

    def send_message(self, msg):
        if self.server_url:
            payload = {"message": msg}
            self.session.post(f"{self.server_url}/message", json=payload)

    def get_latest_message(self):
        if not self.message_queue.empty():
            return self.message_queue.get()
        return None


user_client = ChatHttpClient()
