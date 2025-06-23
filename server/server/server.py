import http.server
import socketserver
import json
import threading
from urllib.parse import urlparse, parse_qs

PORT = 9246

class ChatHandler(http.server.BaseHTTPRequestHandler):
    server_version = "ChatHTTP/0.1"

    connected_clients = set()
    messages = []
    messages_lock = threading.Lock()

    def _send_response(self, code=200, content="", content_type="text/plain"):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        path = urlparse(self.path).path

        client_id = self.client_address[0]  # Use IP as simple client ID

        if path == "/connect":
            # Register client
            self.connected_clients.add(client_id)
            self._send_response(200, "Connected")

        elif path == "/disconnect":
            # Remove client
            self.connected_clients.discard(client_id)
            self._send_response(200, "Disconnected")

        elif path == "/message":
            # Receive a new message JSON: {"message": "..."}
            try:
                data = parse_qs(body)
                msg = data.get("message", [""])[0]

                if msg == "!disc":
                    # Client disconnect request
                    self.connected_clients.discard(client_id)
                    self._send_response(200, "Disconnected")
                    return
                # Add message to shared list
                with self.messages_lock:
                    self.messages.append(f"{client_id}: {msg}")
                self._send_response(200, "Message received")
                print(f"Message from {client_id}: {msg}")
            except Exception as e:
                self._send_response(400, "Bad Request")
        else:
            self._send_response(404, "Not Found")

    def do_GET(self):
        path = urlparse(self.path).path
        client_id = self.client_address[0]

        if path == "/latest-message":
            # Return the latest message (or empty if none)
            with self.messages_lock:
                if self.messages:
                    content = self.messages[-1]
                else:
                    content = ""
            self._send_response(200, content)
        else:
            self._send_response(404, "Not Found")

    def log_message(self, format, *args):
        # Override to disable default logging
        return

if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("", PORT), ChatHandler) as httpd:
        print(f"HTTP Chat Server running on port {PORT}")
        httpd.serve_forever()
