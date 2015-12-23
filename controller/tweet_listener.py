from config import *

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from models import tweet


class MyStreamListener(StreamListener):
	"""docstring for MyStreamListener"""

	def on_status(self, status):

		if status:

			print (status.text)
		

def start():

	myStreamListener = MyStreamListener()
	

	# setup Twitter API connection details
	twitter_auth = OAuthHandler( TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
	twitter_auth.set_access_token( TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET )

	# connect to Twitter Streaming API
	twitter_stream = Stream( twitter_auth, myStreamListener )

	# filter tweets using track, follow and/or location parameters
	# https://dev.twitter.com/streaming/reference/post/statuses/filter
	twitter_stream.filter(track=[ TWITTER_HASHTAG ])
