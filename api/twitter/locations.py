__author__ = 'Gaurav-PC'

import csv
import json
import pycountry
import requests
from pprint import pprint

# import geograpy
# from geograpy import places
# indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\indian_with_date.csv"
#
# pc = places.PlaceContext(['Cleveland', 'Ohio', 'United States'])
# pc.set_countries()
#
# print(pc.countries)
#
# from geograpy import extraction
#
# e = extraction.Extractor(url='http://www.bbc.com/news/world-europe-26919928')
# e.find_entities()
#
# # You can now access all of the places found by the Extractor
# print e.places

url = 'http://open.mapquestapi.com/geocoding/v1/address?key=Kmjtd|luua2qu7n9,7a=o5-lzbgq&location='
headers = {'Referer': 'http://open.mapquestapi.com/geocoding/'}

# locations = []
# with open(indian_file, 'rb') as fp:
#     reader = csv.reader(fp)
#
#     for row in reader:
#         if not row[1] in locations:
#             try:
#                 locations.append(row[1])
#                 r = requests.get(url + row[1], headers=headers)
#                 json_data = json.loads(r.text)
#                 country_code = json_data['results'][0]['locations'][0]['adminArea1']
#                 country = pycountry.countries.get(alpha2=country_code)
#                 pprint(country.name)
#             except Exception as ex:
#                 pprint("global")
#                 continue
# print(len(locations))
# pprint(locations)


class Locations(object):

    def __init__(self):
        self.url = 'http://open.mapquestapi.com/geocoding/v1/address?key=Kmjtd|luua2qu7n9,7a=o5-lzbgq&location='
        self.headers = {'Referer': 'http://open.mapquestapi.com/geocoding/'}

    def get_country(self, location):
        try:
            r = requests.get(self.url + location, headers=self.headers)
            json_data = json.loads(r.text)
            country_code = json_data['results'][0]['locations'][0]['adminArea1']
            country = pycountry.countries.get(alpha2=country_code)
            return country.name
        except Exception as ex:
            print(ex)
            return "global"


if __name__ == "__main__":

    location = "Goa, India"
    cls = Locations()
    country = cls.get_country(location)
    print(country)