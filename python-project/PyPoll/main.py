#pypoll script

import os
import csv
from collections import Counter

election_data = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "Analysis.txt")




with open(election_data, newline = "") as csvfile:

    election_reader = csv.reader(csvfile, delimiter=",")
        
    next(election_reader, None)

    data = [row[2] for row in election_reader]
    counts = Counter(data)
    Max_Votes = max(counts.values())
    Winner = [candidate for candidate, votes in counts.items() if votes == Max_Votes][0]

    listlength = counts.total()
      

with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes: {listlength}\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {round(counts['Charles Casper Stockham']/listlength * 100, 3)}% ({counts['Charles Casper Stockham']})\n")
    txtfile.write(f"Diana DeGette: {round(counts['Diana DeGette']/listlength * 100, 3)}% ({counts['Diana DeGette']})\n")
    txtfile.write(f"Raymon Anthony Doane: {round(counts['Raymon Anthony Doane']/listlength * 100,  3)}% ({counts['Raymon Anthony Doane']})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {Winner} \n")
    txtfile.write("---------------------------\n")

print("Election Results")
print("---------------------------")
print(f"Total Votes: {listlength}")
print("---------------------------")
print(f"Charles Casper Stockham: {round(counts['Charles Casper Stockham']/listlength * 100, 3)}% ({counts['Charles Casper Stockham']})")
print(f"Diana DeGette: {round(counts['Diana DeGette']/listlength * 100, 3)}% ({counts['Diana DeGette']})")
print(f"Raymon Anthony Doane: {round(counts['Raymon Anthony Doane']/listlength * 100,  3)}% ({counts['Raymon Anthony Doane']})")
print("---------------------------")
print(f"Winner: {Winner} ")
print("---------------------------")