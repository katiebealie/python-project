 # pybank script
   
import os
import csv 

budget_data = os.path.join("Resources","budget_data.csv") 
output_file = "Analysis.txt"

Total_Months = []
Net_Total = 0
Average_Changes = []
Max_Increase = (0," ")
Max_Decrease = (0, " ")

with open(budget_data, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter = ",")
    next(budget_reader, None)
    
    previous_row = next(budget_reader)     
    previous_value = int(previous_row[1])  
    
    for row in budget_reader:
       
        Total_Months.append(row[0])
        Net_Total += int(row[1])
        
        current_date = row[0]
        current_value = int(row[1])
        change = current_value - previous_value
        
        Average_Changes.append(round(change, 2))
          
        if change > Max_Increase[0]:
               Max_Increase = (change, current_date)
            
        if change < Max_Decrease[0]:
                Max_Decrease = (change, current_date)
            
        previous_value = current_value
        

# output_file = os.path.join("Analysis", "Analysis.txt")
# with open(output_file) as datafile:
#       writer =  csv.writer(datafile) # for when the csv needs to be changed or written on by the program (?)

#       writer.writerow()

#       writer.writerows()
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {len(Total_Months)}\n")
    txtfile.write(f"Net Total: ${Net_Total}\n")
    txtfile.write(f"Average Change: ${sum(Average_Changes) / len(Average_Changes):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {Max_Increase[1]} (${Max_Increase[0]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {Max_Decrease[1]} (${Max_Decrease[0]})\n")

# Print the analysis results to the terminal

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Net Total: ${Net_Total}")
print(f"Average Change: ${sum(Average_Changes) / len(Average_Changes):.2f}")
print(f"Greatest Increase in Profits: {Max_Increase[1]} (${Max_Increase[0]})")
print(f"Greatest Decrease in Profits: {Max_Decrease[1]} (${Max_Decrease[0]})")

# cleaned_budget = zip() #for when lists need to be zipped together and combined

