 # pybank script
   
#import the right libraries

import os
import csv 

#access the data source files and point to the file to be written on

budget_data = os.path.join("Resources","budget_data.csv") 
output_file = "Analysis.txt"

#define initial variables for the loop
Total_Months = []
Total = 0
Average_Changes = []
Max_Increase = (0," ")
Max_Decrease = (0, " ")

#begin the loop

with open(budget_data, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter = ",")
    next(budget_reader, None) #skip the first row
    
    previous_row = next(budget_reader)     
    previous_value = int(previous_row[1])  

    budget_reader = csv.reader(csvfile, delimiter = ",") #reset the loop
    Total_Months.append(previous_row)
    Total += int(previous_row[1])
    #next(budget_reader1, None)
    for row in budget_reader:
        
        Total_Months.append(row[0])
        Total += int(row[1])
        
        current_date = row[0]
        current_value = int(row[1])
        change = current_value - previous_value
        
        Average_Changes.append(round(change, 2))
          
        if change > Max_Increase[0]:
               Max_Increase = (change, current_date)
            
        if change < Max_Decrease[0]:
                Max_Decrease = (change, current_date)
            
        previous_value = current_value
        
#write the results in the analysis text file

with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {len(Total_Months)}\n")
    txtfile.write(f"Total: ${Total}\n")
    txtfile.write(f"Average Change: ${sum(Average_Changes) / len(Average_Changes):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {Max_Increase[1]} (${Max_Increase[0]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {Max_Decrease[1]} (${Max_Decrease[0]})\n")

#present the results in the terminal

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${Total}")
print(f"Average Change: ${sum(Average_Changes) / len(Average_Changes):.2f}")
print(f"Greatest Increase in Profits: {Max_Increase[1]} (${Max_Increase[0]})")
print(f"Greatest Decrease in Profits: {Max_Decrease[1]} (${Max_Decrease[0]})")



