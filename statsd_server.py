import socket

HOST = "127.0.0.1"
PORT = 8125

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print(f"StatsD server started on {HOST}:{PORT}")

while True:
    data, address = server.recvfrom(1024)

    message = data.decode("utf-8")

    print(f"Received from {address}: {message}")
