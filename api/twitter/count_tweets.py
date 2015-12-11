import csv

indian_file = ""
mideast_file = ""
chinese_file = ""
italian_file = ""


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
                if count == 1:
                    continue
                else:
                    count += 1

        cls.key_val[cuisine] = count

if __name__ == '__main__':
    obj = Count_tweets()
    obj.count(indian_file, 'indian')
    obj.count(mideast_file, 'mid-east')
    obj.count(chinese_file, 'chinese')
    obj.count(italian_file, 'italian')
    obj.write_data()




