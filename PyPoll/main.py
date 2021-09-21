#import dependencies
import os
import csv
import numpy as np

# set filepath
election_data_csv = os.path.join(  "Resources", "election_data.csv")


# open the csv data, skip past the header and count rows (votes)
with open(election_data_csv,) as csv_file:
    csv_header = next(csv_file) 
    csv_reader = csv.reader(csv_file, delimiter=",")
    poll_data = list(csv_reader)
    row_count = len(poll_data)

    
 # Make list of all candidates - list names only one time   
    many_candidates = [item[2] for item in poll_data]
    candidates = list(set(many_candidates))
   

# Initialize variables for vote counting
    vKhan = 0
    vOTooly = 0
    vLi = 0
    vCorrey = 0

# Tally up votes for each of the candidates   
    for i in many_candidates:
        if i == "Khan":
            vKhan += 1
        
        elif i == "O'Tooley":
            vOTooly += 1

        elif i == "Correy":
            vCorrey += 1

        elif i == "Li":
            vLi += 1

 
# Divide candidate votes by total votes to get percentage votes    
    p_khan = ((vKhan/row_count) *100)
    p_Correy = ((vCorrey/row_count) *100)
    p_Li = ((vLi/row_count) *100)
    p_OTooly = ((vOTooly/row_count) *100)

# Find the Winner
    election = [vKhan,vCorrey,vOTooly,vLi]
    winner = max(election)

# Print results to terminal  
    print ("\nElection Results")
    print("------------------------------------")
    print(f'Total Votes: {row_count}') 
    print("------------------------------------\n ")
    print(f"Khan:     {format(p_khan, '.2f')} %     ({vKhan})")
    print(f"Correy:   {format(p_Correy, '.2f')} %   ({vCorrey})")
    print(f"O'Tooley: {format(p_OTooly, '.2f')} %   ({vOTooly})")
    print(f"Li:       {format(p_Li, '.2f')} %       ({vLi})")
    print("\n ----------------------------------")
    print(f"Winner: Khan {winner} !")
    print("------------------------------------")


# print to terminal and to a csv file
with open("PyPoll.txt", "a") as f:
    print('-------------------------------------',file = f)
    print ("\nElection Results", file=f)
    print("------------------------------------", file=f)
    print(f'Total Votes: {row_count}', file=f) 
    print(" ------------------------------------\n ")
    print(f"Khan:     {format(p_khan, '.2f')} %     ({vKhan})", file=f)
    print(f"Correy:   {format(p_Correy, '.2f')} %   ({vCorrey})", file=f)
    print(f"O'Tooley: {format(p_OTooly, '.2f')} %   ({vOTooly})", file=f)
    print(f"Li:       {format(p_Li, '.2f')} %       ({vLi})", file=f)
    print("\n ----------------------------------", file=f)
    print(f"Winner: Khan {winner} !", file=f)
    print("------------------------------------", file=f)