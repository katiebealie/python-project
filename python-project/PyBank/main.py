 # pybank script
   
import os
import csv #making sure the right libraries are imported

budget_data = os.path.join("..", "Resources", "budget_data.csv") #path to file to be read and analyzed


Total_Months = []
Net_Total = 0
Average_Changes = []
Max_Increase = (0," ")
Max_Decrease = (0, " ")

with open(budget_data, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter = ",")
    budget_reader._next_(budget_reader)

    previous_row = next(budget_reader)     
    previous_value = int(previous_row[1])  
    
    for row in budget_reader:
        Total_Months.append(row[0])
        Net_Total += int(row[1])
        
        current_date = row[0]
        current_value = int(row[1])
        change = current_value - previous_value
        
        Average_Changes.append(budget_reader.mean(row[1]))
          
        if change > Max_Increase[0]:
               Max_Increase = (change, current_date)
            
        if change < Max_Decrease[0]:
                Max_Decrease = (change, current_date)
            
        previous_value = current_value
        

print("Total Months:", len(Total_Months))
print ("Net Total:", Net_Total)
print("Average Change:", sum(Average_Changes) / len(Average_Changes))
print("Greatest Increase in Profits:", Max_Increase[1], "($", Max_Increase[0], ")")
print("Greatest Decrease in Profits:", Max_Decrease[1], "($", Max_Decrease[0], ")")
 
 
 #so the results are printed in terminal and the graders know everything worked

 #start the loop, let the robot know where to start and stop reading the csv

zip() #for when lists need to be zipped together and combined
    
csv.writer() #for when the csv needs to be changed or written on by the program (?)