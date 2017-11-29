import tweepy

# from src.token import Token
from src.filter import Filter

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        nyan = Filter()

        # ここのshiotomohackを自分のユーザネームにする
        if str(status.user.screen_name) == "shiotomohack":
            nyan.nyan_filter(status)
