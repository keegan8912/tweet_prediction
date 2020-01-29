import re
import codecs

corpus_raw = u""
file_name = "tweets_trump.txt"

with codecs.open("tweets_trump.txt", 'r') as tweet_text:
    corpus_raw += tweet_text.read()
print("Corpus is {0} char long".format(len(corpus_raw)))

# Remove http links
corpus_clean = re.sub(r'http://\S+|https://\S+|https:|http', '', corpus_raw)
# Replace '&amp' with '&'
corpus_clean = re.sub(r'&amp', '&', corpus_clean)
with open("clean_tweets.txt", 'w') as file_:
    file_.write(corpus_clean)
        