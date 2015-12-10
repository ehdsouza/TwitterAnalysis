__author__ = 'Gaurav-PC'

import csv
from pprint import pprint

indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\indian_cuisine_final.csv"
indian_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\indian_aggregate_countries.csv"

class AggregateCountries(object):

    @classmethod
    def aggregate_india(cls):

        with open(indian_file, 'rb') as fp:

            reader = csv.reader(fp)

            countries = {}
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    if row[2] == 'global':
                        row[2] = 'India'

                    if not countries.has_key(row[2]):
                        countries[row[2]] = {
                            'count': 1
                        }
                    else:
                        countries[row[2]]['count'] += 1

            with open(indian_out_file, 'wb') as op:
                writer = csv.writer(op)
                writer.writerow(['Country', 'Tweet Count'])

                for item in countries.keys():
                    # print([item, countries[item]['count']])
                    writer.writerow([item, countries[item]['count']])
            # pprint(countries)

if __name__ == '__main__':
    cls = AggregateCountries()
    cls.aggregate_india()