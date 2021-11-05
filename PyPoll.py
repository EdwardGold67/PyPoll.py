
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "Election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "Election_analysis.txt")

#1. Initialize a total vote counter
total_vote = 0

#Declare a new list
candidate_options = []

#Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file object with the reader function
    file_reader = csv.reader(election_data)

        #Read the header row
    headers = next(file_reader)

#Print each row in the csv file
    for row in file_reader:
        # 2. Add to the total vote count
        total_vote += 1

     # Print canidate name from each row
        candidate_name = row[2]
#If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

    # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

#print the candidate list
print(candidate_options)



