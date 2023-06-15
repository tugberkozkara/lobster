import json


def is_user_valid(username, password):
    with open("./users.json", "r") as file:
        user_list = json.load(file)["user_list"]
        for user in user_list:
            if username == user["username"] and password == user["password"]:
                return True
        return False
