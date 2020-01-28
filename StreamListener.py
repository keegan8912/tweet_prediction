import tweepy
import json


class MyStreamListener(tweepy.StreamListener):

    # def __init__(self, api: tweepy.API):
    #     super().__init__(api)
    #     self.api = api
    #     self.me = api.me()

    def on_status(self, tweet):
        print("Received status.")
        if self.is_mentioned(tweet):
            username = tweet.user.screen_name
            text = tweet.text
            print(f"{username}: {text}")
            self.api.update_status(f"Hey @{username}, what's up?", in_reply_to_status_id=tweet.id)

    def on_error(self, status):
        print("Error detected")

    @staticmethod
    def is_mentioned(tweet) -> bool:
        for mention in tweet.entities['user_mentions']:
            if mention['screen_name'] == 'sarcastic_trump':
                return True
        return False
