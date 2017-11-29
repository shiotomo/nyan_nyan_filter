import json

class Recorder:
    def __init__(self):
        pass

    def dir_json(self, token):
        with open('./json/token.json', 'w') as f:
            json.dump(token, f, indent=4)
