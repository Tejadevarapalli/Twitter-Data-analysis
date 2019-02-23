import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
consumer_key = "f4qQNYSFaGxO4iB6SamtIZarf"
consumer_secret = "PTuSFEtZAeRP9nov16hJTWQzFNedKTSDKR9ZSS1Iu65JiSbXvO"
access_token = "1089997729219178496-BvhcwdDw6eGPbPJM5wJYqOvsq7rE7G"
access_token_secret = "xZu9ILsesdPiRi5quCxx94mQTfrj00sMEedGrddvYOmsQ"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            with open('pulwama.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'stock market'
    stream.filter(track=['pulwama'])