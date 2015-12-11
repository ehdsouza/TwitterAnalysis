__author__ = 'Gaurav-PC'

import csv
from pprint import pprint

indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\indian_cuisine_final.csv"
mideast_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\mideast\\mideast_cuisine_final.csv"
chinese_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\china\\chinese_cuisine_final.csv"
italian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\italy\\italian_cuisine_final.csv"

italian_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\italy\\italian_aggregate_countries.csv"
chinese_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\china\\chinese_aggregate_countries.csv"
indian_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\indian_aggregate_countries.csv"
mideast_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\mideast\\mideast_aggregate_countries.csv"

class AggregateCountries(object):

    @classmethod
    def aggregate_india(cls):
        cls.process_aggregation(indian_file, indian_out_file)
        return

    @classmethod
    def aggregate_mideast(cls):
        cls.process_aggregation(mideast_file, mideast_out_file)
        return

    @classmethod
    def aggregate_chinese(cls):
        cls.process_aggregation(chinese_file, chinese_out_file)
        return

    @classmethod
    def aggregate_italian(cls):
        cls.process_aggregation(italian_file, italian_out_file)
        return

    @classmethod
    def process_aggregation(cls, in_file, out_file):
        with open(in_file, 'rb') as fp:

            reader = csv.reader(fp)

            countries = {}
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    if row[2] == 'global':
                        row[2] = 'Italy'

                    if not countries.has_key(row[2]):
                        countries[row[2]] = {
                            'count': 1
                        }
                    else:
                        countries[row[2]]['count'] += 1

            with open(out_file, 'wb') as op:
                writer = csv.writer(op)
                writer.writerow(['Country', 'Tweet Count'])

                for item in countries.keys():
                    # print([item, countries[item]['count']])
                    writer.writerow([item, countries[item]['count']])
            # pprint(countries)

if __name__ == '__main__':
    cls = AggregateCountries()
    # cls.aggregate_india()
    # cls.aggregate_mideast()
    # cls.aggregate_chinese()
    cls.aggregate_italian()