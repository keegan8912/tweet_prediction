import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("mm2XCU9YPq3FJC1pxoxS1GXtI",
    "PEJ02bzJOWh4Zb2jBSD5trPLRWAByDca95ffzHnyF1XPmanH5E")
auth.set_access_token("813020461-qZjLAsZffRfhc9B8HIE4AJ3YvJQnwwRIPEArKs2N",
    "Pdac54HObxtfn6MrGIYck1dLtUwI4P8rJ239LeLcz8Mj8")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Hello World!")
