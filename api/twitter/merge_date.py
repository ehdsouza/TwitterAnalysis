__author__ = 'Gaurav-PC'

import csv

temp_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\cuisine_dataset_clean.csv"
indian_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\indian_full.csv"
mideast_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\mideast_full.csv"
write_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\mideast_with_date.csv"

indian_cuisine = ['biryani', 'indian', 'india', 'masala', 'tikka',
                  'naan', 'kulcha', 'upma', 'idli', 'dosa', 'sambar',
                  'rasam', 'kheer', 'tandoori', 'makhni', 'daal', 'dal',
                  'pulao', 'paneer', 'gobi', 'aaloo', 'bhindi', 'rava',
                  'malai', 'kofta', 'sheera', 'puri', 'pani', 'masala dosa',
                  'namkeen', 'samosa', 'vada', 'chutney', 'bhurji', 'bhel', 'chaat',
                  'ragda', 'shev', 'choley', 'kulfi', 'lassi', 'gulab', 'jamun', 'kala',
                  'raj', 'bhog', 'bhajia', 'bhujia', 'rasgulla', 'rasmalai', 'sandesh',
                  'momo', 'tadka', 'kashmir', 'barfi', 'goan', 'south indian', 'north indian',
                  'rajasthani', 'jalebi', 'laddoo', 'papad', 'kolhapuri', 'raita', 'mangalorean',
                  'xacuti', 'rachedo', 'saag', 'sarso', 'gulkand', 'paan']

count = 0
with open(temp_file, 'rb') as tp:
    reader = csv.reader(tp)

    dates = []
    # for row in reader:
    #     dates.append(row[7])
    #     count += 1
    #     if count == 18588:
    #         break

    for row in reader:
        if count <= 18588:
            count += 1
            continue
        else:
            dates.append(row[7])
            count += 1
            if count == 25456:
                break


#
#     for temp_row in tp:
#         tweet_text = temp_row[12]
#
#         if any(word in tweet_text.lower().split() for word in indian_cuisine):
#             count += 1
#
#     print(count)

    with open(mideast_file, 'rb') as fp:
        reader = csv.reader(fp)

        with open(write_file, 'wb') as wp:
            writer = csv.writer(wp)
            writer.writerow(['Date', 'Location', 'Text', 'Sentiment'])

            count = 0
            for file_row in reader:
                # print(indian_row)
                if count == 0:
                    count += 1
                    continue
                row = [dates[count]] + file_row
                # print(row)
                writer.writerow(row)
                count += 1
    #
    # print(count)

