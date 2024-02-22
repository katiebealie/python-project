#pypoll script

#import the right libraries
import os
import csv
from collections import Counter

#access the source data file

election_data = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "Analysis.txt")


#loop through the data and count each vote

with open(election_data, newline = "") as csvfile:

    election_reader = csv.reader(csvfile, delimiter=",")
        
    next(election_reader, None) #make sure to skip the header row

    data = [row[2] for row in election_reader]
    counts = Counter(data)
    Max_Votes = max(counts.values())
    Winner = [candidate for candidate, votes in counts.items() if votes == Max_Votes][0]

    listlength = counts.total()

#name the headers as variables for ease      

Stockham = round(counts['Charles Casper Stockham']/listlength * 100, 3) #percentage of votes
DeGette = round(counts['Diana DeGette']/listlength * 100, 3) #percentage of votes
Doane = round(counts['Raymon Anthony Doane']/listlength * 100,  3) #percentage of votes
Stockham_votes = counts['Charles Casper Stockham'] #individual vote count
DeGette_Votes = counts['Diana DeGette'] #individual vote count
Doane_votes = counts['Raymon Anthony Doane'] #individual vote count
Total_Votes = listlength #count of all votes submitted

#write the results in the text file

with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes: {listlength}\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {Stockham}% ({Stockham_votes})\n")
    txtfile.write(f"Diana DeGette: {DeGette}% ({DeGette_Votes})\n")
    txtfile.write(f"Raymon Anthony Doane: {Doane}% ({Doane_votes})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {Winner} \n")
    txtfile.write("---------------------------\n")

#present the results in the terminal as well

print("Election Results")
print("---------------------------")
print(f"Total Votes: {listlength}")
print("---------------------------")
print(f"Charles Casper Stockham: {Stockham}% ({Stockham_votes})")
print(f"Diana DeGette: {DeGette}% ({DeGette_Votes})")
print(f"Raymon Anthony Doane: {Doane}% ({Doane_votes})")
print("---------------------------")
print(f"Winner: {Winner} ")
print("---------------------------")