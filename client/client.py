import socket
from utils import song_utils

SERVER1_HOST = "127.0.0.1"
SERVER1_PORT = 5001
SERVER2_HOST = "127.0.0.1"
SERVER2_PORT = 5002


def get_command(client1, client2):
    client1.send("get".encode())
    server1_response = client1.recv(1024).decode()
    client2.send("get".encode())
    server2_response = client2.recv(1024).decode()
    if server1_response == server2_response:
        print("\n" + server1_response)
    else:
        print("Error occurred while getting the list of songs.")


def check_command(song_name, client1, client2):
    server1_response, server2_response = song_utils.check_song_existence(song_name, client1, client2)
    if server1_response and server2_response:
        print(f"Song '{song_name}' found in both servers.")
    elif server1_response and not server2_response:
        print(f"Song '{song_name}' found in server1.")
    elif not server1_response and server2_response:
        print(f"Song '{song_name}' found in server2.")
    else:
        print(f"Song '{song_name}' not found in any server.")


def download_command(song_name, client1, client2):
    server1_response, server2_response = song_utils.check_song_existence(song_name, client1, client2)
    if server1_response and server2_response:
        server_choice = input("Choose your preferred server 1 or 2: ")
        if server_choice == "1":
            song_utils.download_song(song_name, client1)
        elif server_choice == "2":
            song_utils.download_song(song_name, client2)
        else:
            print("Invalid server selection.")
            return
    elif server1_response and not server2_response:
        song_utils.download_song(song_name, client1)
    elif not server1_response and server2_response:
        song_utils.download_song(song_name, client2)
    else:
        print(f"Song '{song_name}' not found in any server.")


def exit_command(client1, client2):
    client1.send("exit".encode())
    client2.send("exit".encode())
    client1.close()
    client2.close()


def is_authenticated(client1, client2):
    authenticated = False
    while not authenticated:
        username = input("Enter username: ")
        password = input("Enter password: ")
        client1.send(str("auth "+username+" "+password).encode())
        client2.send(str("auth "+username+" "+password).encode())
        server1_auth_response = client1.recv(1024).decode()
        server2_auth_response = client2.recv(1024).decode()
        if server1_auth_response == "AuthSuccess" and server2_auth_response == "AuthSuccess":
            print("\nLogged in successfully.")
            authenticated = True
            break
        print("\nInvalid username or password.")
    return authenticated


def handle_commands(client1, client2):

    is_authenticated(client1, client2)

    while True:
        print("\nget            Gets the list of songs from the server.\ncheck          Check if a song exists in database.\ndownload       Download a song from song list.\nexit           Exit the program.\n")
        command = input("Enter the command:  ")

        if command.split(" ", 1)[0] == "get":
            get_command(client1, client2)

        elif command.split(" ", 1)[0] == "check":
            song_name = command.split(" ", 1)[1]
            check_command(song_name, client1, client2)

        elif command.split(" ", 1)[0] == "download":
            song_name = command.split(" ", 1)[1]
            download_command(song_name, client1, client2)

        elif command == "exit":
            exit_command(client1, client2)
            break
        else:
            print("Invalid command.")


def start_client():
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((SERVER1_HOST, SERVER1_PORT))
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2.connect((SERVER2_HOST, SERVER2_PORT))

    handle_commands(client1, client2)


if __name__ == "__main__":
    start_client()
