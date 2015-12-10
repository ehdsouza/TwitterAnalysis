__author__ = 'Gaurav-PC'

import csv
import operator
from pprint import pprint
import dateutil.parser as parser

indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\india\\indian_cuisine_final.csv"
mideast_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\mideast\\mideast_cuisine_final.csv"
indian_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\india\\indian_aggregate_years.csv"
mideast_out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\mideast\\mideast_aggregate_years.csv"

class AggregateDates(object):

    @classmethod
    def aggregate_india(cls):
        cls.process_aggregation(indian_file, indian_out_file)
        return

    @classmethod
    def aggregate_mideast(cls):
        cls.process_aggregation(mideast_file, mideast_out_file)
        return


    @classmethod
    def process_aggregation(cls, in_file, outfile):

        with open(in_file, 'rb') as fp:

            reader = csv.reader(fp)

            year_dict = {}
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    sentiment = row[4]
                    year = str(parser.parse(row[0]).year)
                    year = "'" + year + "'"
                    if not year_dict.has_key(year):
                        year_dict[year] = {
                            'pos': 0,
                            'neg': 0,
                            'neutral': 0
                        }
                        year_dict[year][sentiment] += 1

                    else:
                        year_dict[year][sentiment] += 1

            with open(outfile, 'wb') as op:
                writer = csv.writer(op)
                writer.writerow(['Year', 'Positive', 'Negative', 'Neutral'])

                for item in year_dict.keys():
                    # print([item, countries[item]['count']])
                    writer.writerow([item, year_dict[item]['pos'], year_dict[item]['neg'], year_dict[item]['neutral']])
                # pprint(year_dict)

        sortedlist = []
        with open(outfile, 'rb') as fp:
                reader = csv.reader(fp)

                sortedlist = sorted(reader, key=operator.itemgetter(0))
                pprint(sortedlist)

        with open(outfile, 'wb') as op:
                writer = csv.writer(op)
                writer.writerow(['Year', 'Positive', 'Negative', 'Neutral'])

                count = 0
                for item in sortedlist:
                    if count == len(sortedlist)-1:
                        break

                    writer.writerow(item)
                    count += 1

if __name__ == '__main__':
    cls = AggregateDates()
    # cls.aggregate_india()
    cls.aggregate_mideast()