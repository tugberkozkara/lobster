import json
import os


def is_song_name_in_list(song_name):
    with open("./songs.json", "r") as file:
        song_list = json.load(file)["song_list"]
        for song in song_list:
            if song_name == song["name"]:
                return True
        return False


def is_song_file_in_server(server_number, song_name):
    folder_path = f"songs{server_number}/{song_name}.mp3"
    return os.path.exists(folder_path)


def is_song_exists(song_name, server_number):
    if is_song_name_in_list(song_name):
        print(f"Song '{song_name}' found in list. Checking for location...")
        if is_song_file_in_server(server_number, song_name):
            print(f"Song '{song_name}' found in server{server_number}.")
            return True
        else:
            print(f"Song '{song_name}' not found in server{server_number}.")
    else:
        print(f"Song '{song_name}' not found in server{server_number}.")
    return False


def get_song_list():
    with open("./songs.json", "r") as file:
        song_list = json.load(file)["song_list"]
        song_name_list = [song["name"] for song in song_list]
        return song_name_list


def get_song_mp3(song_name, server_number):
    if is_song_name_in_list(song_name):
        with open(f"./songs{server_number}/{song_name}"+".mp3", "rb") as file:
            mp3_file = file.read()
            return mp3_file
