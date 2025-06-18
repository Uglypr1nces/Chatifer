# api_wrapper.py
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from server.server.server_management import *

import socket

app = FastAPI()

TCP_SERVER_ADDR = ("localhost", 9246)
HEADER_SIZE = 64 
FORMAT = "utf-8"

@app.post("/send-data")
async def send_data(request: Request):
    try:
        # Get raw request data (bytes)
        raw_data = await request.body()

        # Optional: print what Django sends
        print(f"Received from Django: {raw_data}")

        # Create a TCP socket and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(TCP_SERVER_ADDR)

            # Send message length first
            msg_length = str(len(raw_data)).encode(FORMAT)
            msg_length += b' ' * (HEADER_SIZE - len(msg_length))
            client_socket.send(msg_length)

            # Then send the actual message
            client_socket.send(raw_data)

            # Receive response
            response = client_socket.recv(2048)  # or larger depending on expected size
            return PlainTextResponse(response.decode(FORMAT))

    except Exception as e:
        print("Error:", e)
        return PlainTextResponse(f"Error: {str(e)}", status_code=500)
