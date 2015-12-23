from peewee import *

tweetsdb = SqliteDatabase('tweets.db')

class Tweet(Model):
	"""Model class for Tweet"""

	class Meta(object):
		database = tweetsdb