import tweepy

from src.token import Token
from src.recorder import Recorder
from src.stream import StreamListener
from src.reader import Reader

class Mode:
    def __init__(self, api_key):
        self.api_key = api_key

    def select(self):
        print("")
        print("Select mode")
        print("1:server")
        print("2:update token")
        print("another:exit")
        mode = input("=> ")
        return mode

    def server(self):
        stream = tweepy.Stream(self.api_key.auth, StreamListener())

        while True:
            try:
                stream.userstream()
            except:
                pass

    def update_token(self):
        token = Token()
        recorder = Recorder()

        keys = token.key_submit()
        recorder.dir_json(keys)
