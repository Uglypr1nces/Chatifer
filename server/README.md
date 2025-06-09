# Chatify Server

Welcome to Chatify! This is the server used for the chatroom.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)

## Features

- Real-time communication between multiple clients.
- Online.

## Requirements

- Python 3.x
- [socket](https://docs.python.org/3/library/socket.html) module (should be available by default)

## Usage

1. **Clone the Repository:**
   ```bash
   cd server
   ```

2. **Download ngrok at https://ngrok.com/**

3. **Move ngrok.exe in the server folder**

4. **Run ngrok**
   ```bash
   ngrok.exe tcp 8000
   ```
4. **Run python server (in a seperate terminal)**
   ```bash
   python3 main.py
   ```
