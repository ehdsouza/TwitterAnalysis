import urllib
import urllib2

class Classifier:
    """
    Classifier class to analyze sentiments of sentences.
    """

    def getSentiment(self, text, language="english"):
        """
        The function that returns a sentiment for text.
        :param text: Text to analyze.
        :param language: Language for the text.
        :return: positive, negative, neutral.
        """

        url = 'http://text-processing.com/demo/sentiment/'
        params = urllib.urlencode({
          'language': language,
          'text': text
        })
        response = urllib2.urlopen(url, params).read()

        # print(response)

        positive = "<strong class='large positive'>"
        negative = "<strong class='large negative'>"
        neutral = "<strong class='large quiet'>"

        if positive in response:
            return "positive"
        elif negative in response:
            return "negative"
        elif neutral in response:
            return "neutral"

#### TEST ####
clsfy = Classifier()
print(clsfy.getSentiment("I love Music"))