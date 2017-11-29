import json

class Reader:
    def __init__(self):
        pass

    def read_dictionary(self):
        pass

    def json_dir(self):
        with open('./json/token.json', 'r') as f:
            token = json.load(f)
        return token
