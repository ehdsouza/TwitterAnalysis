__author__ = 'Gaurav-PC'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import time
import json
import tweepy
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('E:\Developer_Workspaces\Twitter.config')

# variables that contain the user credentials to access twitter apis
access_token = config.get('DEFAULT', 'access_token')
access_token_secret = config.get('DEFAULT','access_token_secret')
consumer_key = config.get('DEFAULT','consumer_key')
consumer_secret = config.get('DEFAULT','consumer_secret')

# define tweet file
tweet_file = None

class TwitterFeeds(object):

    @classmethod
    def get_auth(cls):
        # define auth object
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

    @classmethod
    def get_tweets(cls, keyword):
        # get the auth
        auth = cls.get_auth()
        # define the listener
        listener = StdOutListener()
        # define stream object
        stream = Stream(auth, listener)

        # define the api object
        api = tweepy.API(auth)

        current_milli_time = str(int(round(time.time() * 1000)))
        # open a file to write tweets
        tweet_file = open(keyword+'_'+current_milli_time+'.txt', 'w')

        try:
            # get past tweets, max 500
            result = tweepy.Cursor(api.search, q=keyword).items(10)
            for tweet in result:
                tweet_file.write(tweet.text.encode("UTF-8"))
                tweet_file.write('\n')
                #pprint(tweet)

            stream.filter(track=[keyword])
        except Exception as ex:
            print(ex.message, ex)
        finally:
            tweet_file.close()


class StdOutListener(StreamListener):
    count = 0
    def on_data(self, data):
        self.count+=1
        print(self.count)
        tweet_file.write(json.loads(data)['text'].encode("UTF-8") + '\n')
        #print(json.loads(data)['text'])
        return True

    def on_error(self, status_code):
        print(status_code)

if __name__ == '__main__':
    feeds = TwitterFeeds()
    feeds.get_tweets('paris')



