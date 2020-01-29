import markovify

with open('data/clean_tweets.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5):
    print('NEW SENTENCE : ')
    print(text_model.make_sentence())

for i in range(3):
    print('NEW TWEET : ')
    print(text_model.make_short_sentence(240))