# Retrieve Data we need
# Count the total number of votes
# Create a list of all candidates
# Count the votes each candidated received.
# Calculate the % of total votes each candidate received.
# Who was the winner of the election - person with the most votes.

# Add out dependencies
import csv
import os

# Assign a variable for file to load with path (indirect method)
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and anlalyze data here
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
