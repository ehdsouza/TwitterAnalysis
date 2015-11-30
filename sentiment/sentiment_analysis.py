__author__ = 'Gaurav-PC'

import re
import json
import indicoio
from pprint import pprint
indicoio.config.api_key = 'feb779d7bb3f772b893d6747f22ba631'

class SentimentAnalysis(object):

    @classmethod
    def analyse_sentiments(cls, dict):
        pass

    @classmethod
    def to_dict(cls, file):
        d = dict()
        count = 0

        with open(file, 'r') as f:
            for line in f:
                if line not in ['\n', '\r\n']:
                    line = line.rstrip()
                    _json = json.loads(line)

                    try:
                        tweet = _json['text']
                        d[count] = {
                            'tweet': tweet
                        }
                        count += 1
                        #cls.process_tweet(tweet)
                    except Exception as ex:
                        print(_json)

        if not f.closed:
            f.close()

        pprint(d)

    @classmethod
    def process_tweet(cls, tweet):
        # y = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", tweet).split())
        y = lambda x: re.compile('#').sub('', re.compile('RT @').sub('@', x, count=1).strip())
        print(y(tweet))

if __name__ == '__main__':
    cls = SentimentAnalysis()
    cls.to_dict('E:\Developer_Workspaces\Python_Workspace\sentiment-analysis\paris_op.txt')

    text = [
        "this is such a bright day.",
        "I hate american food!"
    ]

    #result = indicoio.sentiment(text)
    #pprint(result)