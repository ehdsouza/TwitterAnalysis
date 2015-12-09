__author__ = 'Gaurav-PC'

import csv
import indicoio
from pprint import pprint


class IndicoSentimentAnalyser(object):

    def __init__(self):
        indicoio.config.api_key = 'feb779d7bb3f772b893d6747f22ba631'

    @classmethod
    def analyse_sentiments_batch(cls, list):
        try:
            print("Performing batch sentiment analysis for [" + str(len(list)) + "] entries...")
            result = indicoio.sentiment(list)
            sa_result = cls.map_sentiments_batch(result)

            # check number of items
            if len(sa_result) != len(list):
                raise Exception('The input and output list size do not match!')

            return sa_result
        except Exception as ex:
            print("Error occured during analysing sentiments: " + ex)
            return None

    @classmethod
    def analyse_sentiment(cls, text):
        try:
            result = indicoio.sentiment(text)
            sa_result = cls.map_sentiment(result)

            return sa_result
        except Exception as ex:
            print("Error occured during analysing sentiments: " + ex)
            return None

    @classmethod
    def map_sentiments_batch(cls, list):
        """
        Maps decimal values to [pos/neg/neutral]
        > 0.60 : pos
        < 0.40 : neg
        0.40-0.60 : neutral
        :param list:
        :return:
        """
        result = []
        for item in list:
            if item > 0.60:
                result.append("pos")
            elif item < 0.40:
                result.append("neg")
            else:
                result.append("neutral")

        return result

    @classmethod
    def map_sentiment(cls, sentiment):
        """
        Maps decimal values to [pos/neg/neutral]
        > 0.60 : pos
        < 0.40 : neg
        0.40-0.60 : neutral
        :param sentiment:
        :return:
        """
        if sentiment > 0.60:
            return ("pos")
        elif sentiment < 0.40:
            return ("neg")
        else:
            return ("neutral")

if __name__ == '__main__':

    # file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\cuisine_dataset_clean.csv"
    analyser = IndicoSentimentAnalyser()
    #
    # with open(file, "rb") as fp:
    #     reader = csv.reader(fp)
    #
    #     count = 0
    #     lines = []
    #     for row in reader:
    #         lines.append(row[12])
    #         count += 1
    #         if count == 2500:
    #             break

        # pprint(lines)
        # result = analyser.analyse_sentiments(lines)
        # pprint(result)

    text = "I love my India"
    result = analyser.analyse_sentiment(text)
    print result

