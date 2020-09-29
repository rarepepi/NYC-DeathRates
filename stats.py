import csv
import os
path = os.path.dirname(os.path.abspath(__file__))
full_path_in = os.path.join(path, 'New_York_City_Leading_Causes_of_Death.csv')

# Open the data file
def open_data_file():
    with open(full_path_in, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[-1])
# Create data struct for the data


# Do stats on that data


open_data_file()