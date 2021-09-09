# Retrieve Data we need
# Count the total number of votes
# Create a list of all candidates
# Count the votes each candidated received.
# Calculate the % of total votes each candidate received.
# Who was the winner of the election - person with the most votes.

# Add out dependencies
import csv
import os

# Assign a variable to load a file from a path (indirect method being used)
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable for a path to save to a file (indirect method being used)
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)  

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
