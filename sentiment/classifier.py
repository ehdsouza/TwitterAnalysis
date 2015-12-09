import urllib
import urllib2
import json


class Classifier:
    """
    Classifier class to analyze sentiments of sentences.
    """

    def get_sentiment(self, text, language="english"):
        """
        The function that returns a sentiment for text.
        :param text: Text to analyze.
        :param language: Language for the text.
        :return: pos, neg, neutral
        """

        url = 'http://text-processing.com/api/sentiment/'
        params = urllib.urlencode({
          'language': language,
          'text': text
        })
        response = urllib2.urlopen(url, params).read()

        json_response = json.loads(response)

        return json_response["label"]

# TEST #
clsfy = Classifier()
print(clsfy.get_sentiment("I love music"))
