#pypoll script

import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
output_file = "Analysis.txt"

Total_Votes = []
Stockham = 0
DeGette = 0
Doane = 0

with open(election_data, newline = "") as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    next(election_reader, None)
    
    for row in election_reader:
        candidate_name = row[2]
        Total_Votes.append(row[0])
        if candidate_name == "Charles Casper Stockham":
            Stockham += 1
        elif candidate_name == "Diane DeGette":
            DeGette += 1
        elif candidate_name == "Raymon Anthony Doane":
            Doane += 1

    Max_Votes = election_reader.most_common(2)[0]
    print(Max_Votes)
    
            


print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(Total_Votes)}")
print("---------------------------")
print(f"Charles Casper Stockham: {Stockham/Total_Votes}% {Stockham}")
print(f"Diana DeGette: {DeGette/Total_Votes}% {DeGette}")
print(f"Raymon Anthony Doane: {Doane/Total_Votes}% {Doane}")
print("---------------------------")
print(f"Winner: {Max_Votes} ")
