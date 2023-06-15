import socket
from utils import song_utils

SERVER1_HOST = "127.0.0.1"
SERVER1_PORT = 5001
SERVER2_HOST = "127.0.0.1"
SERVER2_PORT = 5002


def get_command(client1, client2):
    client1.send("get".encode())
    server1_response = client1.recv(4096).decode()
    client2.send("get".encode())
    server2_response = client2.recv(4096).decode()
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
        song_utils.download_song(song_name, server_choice)
    elif server1_response and not server2_response:
        song_utils.download_song(song_name, "1")
    elif not server1_response and server2_response:
        song_utils.download_song(song_name, "2")
    else:
        print(f"Song '{song_name}' not found in any server.")


if __name__ == "__main__":

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((SERVER1_HOST, SERVER1_PORT))
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2.connect((SERVER2_HOST, SERVER2_PORT))

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
            client1.close()
            client2.close()
            break
        else:
            print("Invalid command.")
