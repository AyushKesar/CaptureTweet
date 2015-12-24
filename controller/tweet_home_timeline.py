from config import *

from tweepy import OAuthHandler, API


def get_text_cleaned(tweet):
	pass

def start():


	# setup Twitter API connection details
	twitter_auth = OAuthHandler( TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
	twitter_auth.set_access_token( TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET )

	tweet_api = API(twitter_auth)

	public_tweets = tweet_api.home_timeline(count = 1) #count=1 to read only one tweet

	for tweet in public_tweets:

		print ('{}'.format(tweet))
