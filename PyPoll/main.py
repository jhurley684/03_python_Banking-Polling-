import os
import csv
import numpy as np


election_data_csv = os.path.join(  "Resources", "election_data.csv")


# open the csv data, skip past the header and count rows (votes)
with open(election_data_csv,) as csv_file:
    csv_header = next(csv_file) 
    csv_reader = csv.reader(csv_file, delimiter=",")
    poll_data = list(csv_reader)
    row_count = len(poll_data)
    # print(f'Total Votes: {row_count}')  ****Use at bottom for report
    
 # Make list of all candidates - list names only one time   
    many_candidates = [item[2] for item in poll_data]
    # print(many_candidates)
    candidates = list(set(many_candidates))
    # print(f'Candidates who received votes: {candidates}')


# Tally up votes for each of the candidates
# Initialize variables for vote counting
    vKhan = 0
    vOTooly = 0
    vLi = 0
    vCorrey = 0

   
# Count votes for each candidate
    for i in many_candidates:
        if i == "Khan":
            vKhan += 1
        
        elif i == "O'Tooley":
            vOTooly += 1

        elif i == "Correy":
            vCorrey += 1

        elif i == "Li":
            vLi += 1

    
    # print(f"Khan: {vKhan}")
    # print(f"Correy: {vCorrey}")
    # print(f"Li: {vLi}")
    # print(f"O'Tooley: {vOTooly}")

# Divide candidate votes by total votes to get percentage votes    
    p_khan = ((vKhan/row_count) *100)
    p_Correy = ((vCorrey/row_count) *100)
    p_Li = ((vLi/row_count) *100)
    p_OTooly = ((vOTooly/row_count) *100)

# Find the Winner
    election = [vKhan,vCorrey,vOTooly,vLi]
    winner = max(election)

    
    print ("\nElection Results")
    print("------------------------------------")
    print(f'Total Votes: {row_count}') 
    print(" ------------------------------------\n ")
    print(f"Khan:     {format(p_khan, '.2f')} %     ({vKhan})")
    print(f"Correy:   {format(p_Correy, '.2f')} %   ({vCorrey})")
    print(f"O'Tooley: {format(p_OTooly, '.2f')} %   ({vOTooly})")
    print(f"Li:       {format(p_Li, '.2f')} %       ({vLi})")
    print("\n ------------------------------------")
    print(f"Winner: {winner} !")
    print("------------------------------------")

# Print final report (remembering to )