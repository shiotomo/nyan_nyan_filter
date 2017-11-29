import os
import tweepy

from src.token import Token
from src.recorder import Recorder
from src.stream import StreamListener
from src.reader import Reader

def nyan_nyan():
    print("----------------------------------")
    print("--- Nyan Nyan Filter ---")
    print("ver 1.0")
    print("--- Set up server ---")
    print("Nyan nyan ------- OK")
    print("Nyan nyan filter Server set up...")
    print("Nyan nyan filter Server start !!")
    print("----------------------------------")

def main():
    nyan_nyan()
    token = Token()
    recorder = Recorder()
    reader = Reader()

    if not os.path.isdir("./json"):
        os.mkdir("json")
        keys = token.key_submit()
        recorder.dir_json(keys)

    keys = reader.json_dir()

    api_key = token.get_key(keys)

    stream = tweepy.Stream(api_key.auth, StreamListener())

    while True:
        try:
            stream.userstream()
        except:
            pass

if __name__ == '__main__':
    main()
