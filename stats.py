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


# Open the data file
def open_data_file():
    with open(full_path_in) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            _process_row(row)

# Clean the data and create data struct
def _is_valid_row(row):
    if all(v != "." for v in row):
        return True
    return False

def _process_row(row):
    if _is_valid_row(row):
        container = DeathDataContainer(
            row[0], row[1], row[2],
            row[3], row[4], row[5],
            row[6])
        cleaned_data.append(container)

# Do stats on the cleaned data
def find_mean(data):
    return sum(data) / len(data)


def print_all_data():
    for d in cleaned_data:
        print(d)

# ------------ MAIN ------------
def main():
    open_data_file()

if __name__ == '__main__':
    main()
