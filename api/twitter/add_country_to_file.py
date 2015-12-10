__author__ = 'Gaurav-PC'

import csv
from locations import Locations

indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\indian_with_date.csv"
italian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\italian_with_date.csv"
out_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\italian_cuisine_final.csv"

location = Locations()

with open(italian_file, 'rb') as fp:
    reader = csv.reader(fp)

    with open(out_file, 'wb') as op:
        writer = csv.writer(op)
        writer.writerow(['Date', 'Location', 'Country', 'Text', 'Sentiment'])

        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue

            loc = row[1]
            country = location.get_country(loc)
            final = [row[0], loc, country, row[2], row[3]]
            writer.writerow(final)



