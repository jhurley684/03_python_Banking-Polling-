import os
import csv
import numpy as np

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

#Print each list and total amount of months        
    # print(profits_losses)
    # print(months)
    # print(f'Total Months: {len(profits_losses)}')


  
 #Convert elements in profits_losses to int, and make it a list 
    profits_losses = list(map(int, profits_losses))
    
# Sum the profits_losses list to a total  
    Sum_PL = sum(profits_losses)
    # print(f'Total Profit: {Sum_PL}')

    combined = zip(months,profits_losses)
    # print(f'Heres a dictionary of combined {dict(combined)}')
    # print(f'Here is a list of combined {list(combined)}')
    

 

 # Make a list of all the absolute differences between elements
    change = np.diff(profits_losses)
    # print(change)
    # print(len(change))
    Avg_change = (sum(change)/len(change))
    # print(f'Average Changes: {Avg_change}')  #****Use for summary at end

 #Calculate Greatest increase in profits - including dates
    greatest_profits = change.max()
    greatest_losses = change.min()
    # print(f'Greatest increase in profites: {greatest_profits}')
    # print(f'Greatest decrease in profits: {greatest_losses}')


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
    print(f'Total Profit: {Sum_PL}')
    print(f'Average Changes: {Avg_change}')
    print(f'Greatest Increase in Profits: {max_gain}   {greatest_profits}')
    print(f'Greatest Decrease in Profits: {min_gain}   {greatest_losses}')
    print(' ' )
    print(' ' )
    

# print to terminal and to a csv file
with open("PyBank.txt", "a") as f:
    print('-----------------------------------------',file = f)
    print(f'Total Months: {len(profits_losses)}',file = f)
    print(f'Total Profit: {Sum_PL}',file = f)
    print(f'Average Changes: {Avg_change}',file = f)
    print(f'Greatest Increase in Profits: {max_gain}   {greatest_profits}',file = f)
    print(f'Greatest Decrease in Profits: {min_gain}   {greatest_losses}',file = f) 