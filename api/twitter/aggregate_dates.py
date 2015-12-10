__author__ = 'Gaurav-PC'

import csv
from pprint import pprint
import dateutil.parser as parser

indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\indian_cuisine_final.csv"
indian_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\indian_aggregate_years.csv"

class AggregateDates(object):

    @classmethod
    def aggregate_india(cls):

        with open(indian_file, 'rb') as fp:

            reader = csv.reader(fp)

            year_dict = {}
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    sentiment = row[4]
                    year = parser.parse(row[0]).year

                    if not year_dict.has_key(year):
                        year_dict[year] = {
                            'pos': 0,
                            'neg': 0,
                            'neutral': 0
                        }
                        year_dict[year][sentiment] += 1

                    else:
                        year_dict[year][sentiment] += 1

            with open(indian_out_file, 'wb') as op:
                writer = csv.writer(op)
                writer.writerow(['Year', 'Positive', 'Negative', 'Neutral'])

                for item in year_dict.keys():
                    # print([item, countries[item]['count']])
                    writer.writerow([item, year_dict[item]['pos'], year_dict[item]['neg'], year_dict[item]['neutral']])
                # pprint(year_dict)

if __name__ == '__main__':
    cls = AggregateDates()
    cls.aggregate_india()