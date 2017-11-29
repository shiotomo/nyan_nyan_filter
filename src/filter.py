import tweepy

from datetime import datetime

from src.reader import Reader
from src.token import Token

class Filter:
    def __init__(self):
        pass

    def nyan_filter(self, status):
        token = Token()
        reader = Reader()
        api = token.get_key(reader.json_dir())

        print(status.text)
        text = status.text

        # for nyan in nyan_list:
        for nyan in open('./dictionary.txt', 'r'):
            nyan = nyan.replace('\n', '')
            print(nyan)
            if nyan in text:
                print("OUT!! Delete Tweet!! Nyan Nyan Filter Start Up!!")
                for tweet in tweepy.Cursor(api.user_timeline).items():
                    api.destroy_status(tweet.id)
                    break;
                api.update_status("にゃんにゃんフィルター発動!!\n" + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            else:
                print("No problem!!")
