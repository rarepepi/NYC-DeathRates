import csv
import os
path = os.path.dirname(os.path.abspath(__file__))
full_path_in = os.path.join(path, 'New_York_City_Leading_Causes_of_Death.csv')
cleaned_data = []


class DeathDataContainer:
    def __init__(self, year, cause, sex, race, deaths, rate, age_adj_rate):
        self.year = year
        self.cause = cause
        self.sex = sex
        self.race = race
        self.deaths = deaths
        self.rate = rate
        self.age_adj_rate = age_adj_rate

    def __str__(self):
        return f"{self.year} |  {self.cause} | {self.sex} | {self.race} | {self.deaths} | {self.rate} | {self.age_adj_rate}"


def is_valid_row(row):
    if all(v != "." for v in row):
        return True
    return False


def process_row(row):
    if is_valid_row(row):
        container = DeathDataContainer(
            row[0], row[1], row[2],
            row[3], row[4], row[5],
            row[6])
        cleaned_data.append(container)


# Open the data file
def open_data_file():
    with open(full_path_in) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            process_row(row)

# Create data struct for the data


# Do stats on that data


open_data_file()
for d in cleaned_data:
    print(d)