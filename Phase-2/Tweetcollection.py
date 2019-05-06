#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1089997729219178496-BvhcwdDw6eGPbPJM5wJYqOvsq7rE7G"
access_token_secret = "xZu9ILsesdPiRi5quCxx94mQTfrj00sMEedGrddvYOmsQ"
consumer_key = "f4qQNYSFaGxO4iB6SamtIZarf"
consumer_secret = "PTuSFEtZAeRP9nov16hJTWQzFNedKTSDKR9ZSS1Iu65JiSbXvO"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        saveFile = open(r'GOTextraction.json','a')
        saveFile.write(data)
        saveFile.close()
        

    def on_error(self, status):
        print (status)
		
 

if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['GOT', 'got', 'GameofThrones', 'aryastark', 'sansastark', 'jon snow', 'knight king', 'night king', 'tyrion lannister', 'jaime lannister', 'Got', 'bran stark', 'winterfell', 'cersei', 'drogon', 'daenerys'])
