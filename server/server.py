import socket
import threading
from utils import song_utils

HOST = "127.0.0.1"
PORT = 5001

server_number = input("Server number 1 or 2>>> ")
while server_number != "1" and server_number != "2":
    server_number = input("Server number can only be 1 or 2>>> ")

if server_number == "2":
    PORT = 5002


def handle_request(client):
    while True:
        command = client.recv(4096).decode()

        if command == "get":
            client.send(str(song_utils.get_song_list()).encode())

        elif command.split(" ", 1)[0] == "check":
            song_name = command.split(" ", 1)[1]
            response = song_utils.is_song_exists(song_name, server_number)
            client.send(response.to_bytes())

        elif command.split(" ", 1)[0] == "download":
            song_name = command.split(" ", 1)[1]
            mp3_data = song_utils.get_song_mp3(song_name, server_number)
            client.sendall(mp3_data)
            client.send(b'EOF')
            print(f"{song_name}.mp3 sent to {client.getpeername()[0]}:{client.getpeername()[1]}")

        elif command == "exit":
            break

    client.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server{server_number} is running...")

    while True:
        client, address = server.accept()
        print(f"Connected with {address[0]}:{address[1]}")
        client_thread = threading.Thread(target=handle_request, args=(client,))
        client_thread.start()


if __name__ == "__main__":
    start_server()
