import json
import os


class Register:
    """class for register"""

    def __init__(self):
        if not os.path.isfile("register.json"):
            user_list: list = []
            users: dict = {}
            users["users"] = user_list
            with open("register.json", 'w') as f:
                json.dump(users, f)

    def save_in_jason(self, first_name: str, last_name: str, n_code: str, phone: str):
        """save a user information in a json file called her/his full name"""
        user_dict = {}
        user_dict['first_name'] = first_name
        user_dict['last_name'] = last_name
        user_dict['n_code'] = n_code
        user_dict['phone'] = phone
        with open(f"{first_name + last_name}.json", 'w') as file:
            json.dump(user_dict, file)
        self.save_in_general_json_file(first_name,last_name,n_code,phone)

    def save_in_general_json_file(self, first_name: str, last_name: str, n_code: str, phone: str):
        """save a user in general json file that all users there"""
        j_list: list
        with open("register.json", 'r') as f:
            users = json.load(f)

        user_dict = {}
        user_dict['first_name'] = first_name
        user_dict['last_name'] = last_name
        user_dict['n_code'] = n_code
        user_dict['phone'] = phone
        users["users"].append(user_dict)
        with open("register.json", 'w') as f:
            json.dump(users, f)

    def register_json(self, json_file):
        """load a json file to dict and send to register def"""
        with open(json_file, 'r') as file:
            user_dict = json.load(file)
        self.register(**user_dict)

    def register(self, first_name: str, last_name: str, n_code: str, phone: str):
        """register a user By receiving information"""
        print("first_name : ", first_name)
        print("last_name : ", last_name)
        print("n_code : ", n_code)
        print("phone : ", phone)
        print("register done...")
        print("==================================")

    def register_by_general_file(self, general_json_file):
        """load the final user from the general json file and send to register def"""
        with open(general_json_file, 'r') as f:
            users = json.load(f)
        users_list = users["users"]
        self.register(**(users_list[len(users_list) - 1]))


register_obj = Register()
# register_obj.save_in_jason("akbar","asqari","1234","0912123456789")
# register_obj.register_json("aliakbari.json")
# register_obj.register_json("amirtalebi.json")
# register_obj.save_in_general_json_file("amir","talebi","1234","0912123456789")
# register_obj.save_in_general_json_file("amir","akbari","4321","09121114444")
# register_obj.register_by_general_file("register.json")
