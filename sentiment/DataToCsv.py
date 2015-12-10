import csv

"""
For Bar Graph

"""

class DataToCsv:

    def aggregate_data(self, csv_to_proc, output_csv):
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

        for row in reader:
            row_dict = dict(row)
            country = row_dict["Country"].strip()
            if len(country) == 0:
                # If location is blank, consider Global.
                country = "Global"
            if country not in result_dict:
                result_dict[country] = {'country': country,
                                         'positive': 0,
                                         'negative': 0,
                                         'neutral': 0}

            if row_dict["Sentiment"] == "pos":
                result_dict[country]["positive"] += 1
            if row_dict["Sentiment"] == "neg":
                result_dict[country]["negative"] += 1
            if row_dict["Sentiment"] == "neutral":
                result_dict[country]["neutral"] += 1

        csvout = csv.writer(output_csv)
        csvout.writerow(["Country", "Positive", "Negative", "Neutral"])

        for data in result_dict:
            csvout.writerow([data, result_dict[data]["positive"], result_dict[data]["negative"],
                             result_dict[data]["neutral"]])

        csvfile.close()
        output_csv.close()


# TEST #
if __name__ == "__main__":
    datatocsv = DataToCsv()
    csv_proc = "/home/mangirish/BDAA/TwitterAnalysis/csvs/indian_cuisine_final.csv"
    output_csv = "/home/mangirish/BDAA/TwitterAnalysis/csvs/indian_full_agg.csv"
    datatocsv.aggregate_data(csv_proc, output_csv)


