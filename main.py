import os
import tweepy

from src.token import Token
from src.recorder import Recorder
from src.stream import StreamListener
from src.reader import Reader
from src.mode import Mode

def nyan_nyan():
    print("----------------------------------")
    print("-------- Nyan Nyan Filter --------")
    print("---------------------- ver 1.0 ---")
    print("---------- Set up server ---------")
    print("----------------------------------")
    print("Nyan nyan --------------------- OK")
    print("Nyan nyan filter set up...")

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

    mode = Mode(api_key)
    select_number = mode.select()

    print("")

    if (select_number == "1"):
        print("select server !!")
        print("Nyan nyan filter start !!")
        print("----------------------------------\n")
        mode.server()
    elif (select_number == "2"):
        print("select client !!")
        print("Nyan nyan filter start !!")
        print("----------------------------------\n")
        mode.client()
        pass
    elif (select_number == "3"):
        print("select update token !!")
        print("----------------------------------\n")
        mode.update_token()
    else:
        print("See yoo ...")
        pass


if __name__ == '__main__':
    main()
