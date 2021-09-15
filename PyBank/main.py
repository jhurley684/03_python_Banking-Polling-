import os
import csv

budget_data_csv = os.path.join(  "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        print(row)



