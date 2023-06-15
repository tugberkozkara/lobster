import socket

SERVER1_HOST = "127.0.0.1"
SERVER1_PORT = 5001
SERVER2_HOST = "127.0.0.1"
SERVER2_PORT = 5002


def check_song_existence(song_name, client1, client2):
    client1.send(str("check "+song_name).encode())
    server1_response = client1.recv(4096)
    client2.send(str("check "+song_name).encode())
    server2_response = client2.recv(4096)
    return bool.from_bytes(server1_response), bool.from_bytes(server2_response)


def download_song(song_name, server_number):
    if server_number == "1":
        server_address = SERVER1_HOST
        server_port = SERVER1_PORT
    elif server_number == "2":
        server_address = SERVER2_HOST
        server_port = SERVER2_PORT
    else:
        print("Invalid preferred server selection.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_address, server_port))
    client.send(str("download "+song_name).encode())

    mp3_data = b''
    while True:
        data = client.recv(4096)
        if not data or data[-3:] == b'EOF':
            break
        mp3_data += data

    with open("./downloads/" + song_name + ".mp3", "wb") as file:
        file.write(mp3_data)

    print("Downloaded!")
    client.close()
