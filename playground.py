import tweepy
from StreamListener import MyStreamListener
from StandaloneTweeter import StandaloneTweeter

# Authenticate to Twitter
auth = tweepy.OAuthHandler("SUdZqYq6bB0VignOg63Ze5QnK",
    "bOQXiQ3uL8t6qO2gbsWBVAxBZt4Z4eFTcZFrmhwvuLGPCQrHJI")
auth.set_access_token("1222244833441603584-PgG6AZ7nZZxdSaWBIBuRwQUlcSnlnI",
    "wBab28Ek35JbzC0k9wnxmsW3XQWjoRFg3LFvizy9GXcAd")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Setup @sarcastic_trump reply machine
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["sarcastic_trump"], languages=["en"], is_async=True)

# Setup @sarcastic_trump standalone tweet machine
standalone_tweeter = StandaloneTweeter(api)
standalone_tweeter.run_every(minutes=2)
