import datetime

from peewee import *

from models import db_model


class Tweet(db_model.TweetModel):
	message = CharField()
	author = CharField()
	is_valid = BooleanField(default=True)
	is_done = BooleanField(default=False)
	json_data = TextField()
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		order_by = ('-created_at',)

def start():
	db_model.tweetsdb.connect()
	# tweetsdb.create_table([Tweet])
	Tweet.create_table(True)
	db_model.tweetsdb.close()