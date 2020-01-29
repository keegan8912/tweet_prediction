import tweepy
import json
import gpt_2_simple as gpt2
import tensorflow as tf
import re


class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api: tweepy.API):
        super().__init__(api)
        self.api = api
        tf.reset_default_graph()
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sess, run_name='trump_clean_small')

    def generate_gpt2_tweet_using_prefix(self, prefix='Your mum', run_name='trump_clean_small'):
        return gpt2.generate(self.sess, length=40, temperature=0.8, nsamples=1, run_name=run_name, prefix=prefix,
                             return_as_list=True)

    def on_status(self, tweet):
        print("Received status.")
        if self.is_mentioned(tweet):
            username = tweet.user.screen_name
            text = str(tweet.text)
            # do I need to remove @sarcastic_trump before generating a new prediction?
            text_without_self_username = text.replace("@sarcastic_trump", "")

            generated_tweet_from_text_as_prefix = self.generate_gpt2_tweet_using_prefix(prefix=text_without_self_username)
            # remove the extra lines without punctuation. Might also remove hashtags # ?
            tweet_without_extra_lines = self.remove_extra_lines(generated_tweet_from_text_as_prefix[0])
            
            print(f"{username}: {text}")

            if len(generated_tweet_from_text_as_prefix[0])+len(username)+5 > 240:
                self.api.update_status(f"Hey @{username}, {tweet_without_extra_lines[0:240-len(username)-5]}",
                                       in_reply_to_status_id=tweet.id)
            else:
                self.api.update_status(f"Hey @{username}, {tweet_without_extra_lines}", in_reply_to_status_id=tweet.id)

    def on_error(self, status):
        print("Error detected")

    @staticmethod
    def is_mentioned(tweet) -> bool:
        for mention in tweet.entities['user_mentions']:
            if mention['screen_name'] == 'sarcastic_trump':
                return True
        return False

    @staticmethod
    def remove_extra_lines(self, text):
        list_of_suffix = [".", ",", "!", "?"]
        idx = []
        for suffix in list_of_suffix:
            idx.append(text.rfind(suffix))

        for suffix in list_of_suffix:
            if text.endswith(suffix, 0, len(text)):
                #save index, take the largest index here
                return text
            else:
                return text[0:max(idx)+1]
