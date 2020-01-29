import tweepy
import markovify
import schedule
import time

class StandaloneTweeter:

    def __init__(self, api):
        self.api = api
        with open('data/clean_tweets.txt') as f:
            text = f.read()
        self.text_model = markovify.Text(text)

    def tweet(self):
        standalone_tweet = self.text_model.make_short_sentence(240)
        self.api.update_status(f"{standalone_tweet}")

    def run_every(self, minutes):
        schedule.every(minutes).minutes.do(self.tweet)
        while True:
            schedule.run_pending()
            time.sleep(1)
