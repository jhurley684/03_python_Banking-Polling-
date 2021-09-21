#import dependencies
import os
import csv
import numpy as np

#Set filepath
budget_data_csv = os.path.join(  "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")


# print out header and rows in the csv_file
    csv_header = next(csv_reader)  #try csv_reader
    # print(f"Header:{csv_header}")


# write data to lists
#=========================================

#initialize list variables to empty sets
    profits_losses = []
    months=[]

#List all in profits_losses column to profits_losses
#List all in months column to months
    for row in csv_reader:
        profits_losses.append(row[1])
        months.append(row[0])


  
 #Convert elements in profits_losses to int, and make it a list 
    profits_losses = list(map(int, profits_losses))
    

# Sum the profits_losses list to a total  
    Sum_PL = sum(profits_losses)
   

# Create a combined file for months & profits
    combined = zip(months,profits_losses)
  
 
 # Make a list of all the absolute differences between elements
    change = np.diff(profits_losses)
  
  #Add up all the changes then divide by number of changes to get average
    Avg_change = (sum(change)/len(change))


 #Calculate Greatest increase in profits - including dates
    greatest_profits = change.max()

 #Calculate Greatest decrease in profits - including dates 
    greatest_losses = change.min()
 

# Find the date key that goes with the greatest increase & decrease
    combined_d = dict(combined) #this makes the combined list a dictionary
    max_gain = max(combined_d, key=combined_d.get)
    min_gain = min(combined_d, key=combined_d.get)



# Print to terminal the Financial Analysis
    print(' ' )
    print(' ' )
    print('Financial Analysis')
    print('-----------------------------------------')
    print(f'Total Months: {len(profits_losses)}')
    print(f'Total Profit: ${Sum_PL}')
    print(f'Average Changes: ${format(Avg_change, ".2f")}')
    print(f'Greatest Increase in Profits: {max_gain}   ${greatest_profits}')
    print(f'Greatest Decrease in Profits: {min_gain}   ${greatest_losses}')
    print(' ' )
  
    

# print to terminal and to a csv file
with open("PyBank.txt", "a") as f:
    print('-----------------------------------------',file = f)
    print(f'Total Months: {len(profits_losses)}',file = f)
    print(f'Total Profit: {Sum_PL}',file = f)
    print(f'Average Changes: ${format(Avg_change, ".2f")}',file = f)
    print(f'Greatest Increase in Profits: {max_gain}   ${greatest_profits}',file = f)
    print(f'Greatest Decrease in Profits: {min_gain}   ${greatest_losses}',file = f) 