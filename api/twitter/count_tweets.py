import csv

indian_file = "indian_cuisine_final.csv"
mideast_file = "mideast_cuisine_final.csv"
chinese_file = "chinese_cuisine_final.csv"
italian_file = "italian_cuisine_final.csv"


class Count_tweets(object):
    out_file = ''

    key_val = {}

    @classmethod
    def write_data(cls):
        with open(cls.out_file, 'wb') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Cuisine', 'Tweets'])

            for k, v in cls.key_val.iteritems():
                writer.writerow([k, v])

    @classmethod
    def count(cls, in_file, cuisine):
        with open(in_file, 'rb') as fp:

            reader = csv.reader(fp)

            count = 0

            for row in reader:
                count += 1

        cls.key_val[cuisine] = count

if __name__ == '__main__':
    obj = Count_tweets()
    obj.count(indian_file, 'indian')
    obj.count(mideast_file, 'mid-east')
    obj.count(chinese_file, 'chinese')
    obj.count(italian_file, 'italian')
    obj.write_data()




