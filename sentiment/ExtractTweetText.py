import csv

"""
For Word Cloud

"""

class ExtractTweetText:

    def extract(self, csv_to_proc, output_csv):
        """

        :param csv_to_proc: Path to csv file to process.
        :param output_csv: Path to output csv file.
        :return:
        """

        result_dict = dict()

        csvfile = open(csv_to_proc, 'r')
        output_csv = open(output_csv, 'w')

        fieldnames = ("Date","Location","Country","Text","Sentiment")
        reader = csv.DictReader(csvfile, fieldnames)

        csvout = csv.writer(output_csv)

        for row in reader:
            row_dict = dict(row)
            text = row_dict["Text"]
            csvout.writerow([text])

        csvfile.close()
        output_csv.close()


# TEST #
if __name__ == "__main__":
    tweet = ExtractTweetText()
    csv_proc = "/home/mangirish/BDAA/TwitterAnalysis/csvs/indian_cuisine_final.csv"
    output_csv = "/home/mangirish/BDAA/TwitterAnalysis/csvs/indian_full_agg_text.csv"
    tweet.extract(csv_proc, output_csv)


