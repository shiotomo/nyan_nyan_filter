import json
import tweepy

class Token:
    token = {}

    def __init__(self):
        pass

    def key_submit(self):
        self.token["consumer_key"] = input("consumer_key => ")
        self.token["consumer_secret"] = input("consumer_secret => ")
        self.token["access_token"] = input("access_token => ")
        self.token["access_secret"] = input("access_secret => ")

        return self.token

    def get_key(self, token):
        auth = tweepy.OAuthHandler(token["consumer_key"], token["consumer_secret"])
        auth.set_access_token(token["access_token"], token["access_secret"])
        self.api = tweepy.API(auth)

        return self.api
