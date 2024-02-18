#pypoll script

import os
import csv

election_data = os.path.join("..", "Resources", "election_data.csv")

Total_Votes = []
Stockham = []
DeGette = []
Doane = []

with open(election_data, newline = "") as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    for row in election_reader:
        Total_Votes.append()