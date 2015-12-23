from peewee import *

tweetsdb = SqliteDatabase('tweets.db')

class TweetModel(Model):
	"""Model class for Tweet"""

	class Meta(object):
		database = tweetsdb # This model uses the "tweets.db" database.