from config import *

from models import tweet
from controller import tweet_listener


if __name__ == '__main__':

	print ('Starting')

	tweet.start()

	tweet_listener.start()