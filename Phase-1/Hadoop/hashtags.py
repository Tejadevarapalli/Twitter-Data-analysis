import codecs
import json
import sys

def parse_json_tweet(l):
    tw = json.loads(l)
    hashtags = [hashtag['text'] for hashtag in tw['entities']['hashtags']]
    urls = [url['expanded_url'] for url in tw['entities']['urls']]
    return [hashtags, urls]
if __name__ == "__main__":
	json_tweets = codecs.open("C:\\Users\\rahul\PycharmProjects\Tweets.py\pulwama.json", 'r', 'utf-8')
	text_tweets_output = codecs.open("C:\\Users\\rahul\PycharmProjects\Tweets.py\\twitterhashtagsurlsdata.txt", 'w','utf-8')
for line in json_tweets:
    try:
        [htags, urls] = parse_json_tweet(line)
        text_tweets_output.write(str([htags, urls]) + "\n")
    except:
        pass

json_tweets.close()
text_tweets_output.close()