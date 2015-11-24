

__author__ = 'erika'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import configparser

config = configparser.ConfigParser()
config.sections()
config.read('F:\BDAA\config')

# variables that contain the user credentials to access twitter apis
access_token = config.get('DEFAULT', 'access_token')
access_token_secret = config.get('DEFAULT','access_token_secret')
consumer_key = config.get('DEFAULT','consumer_key')
consumer_secret = config.get('DEFAULT','consumer_secret')


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status_code):
        print(status_code)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['goshenoy'])
