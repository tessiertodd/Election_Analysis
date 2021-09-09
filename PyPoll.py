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

# Add total vote counter before opening file statement
total_votes = 0

# Declare an empty list
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Declare and empty string value for winning candidate
winning_candidate=" "
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)  

    # Read and print the header row.
    headers = next(file_reader)

    # Go through all the data in the CSV file and add to the total vote count
    for row in file_reader:
        # Add to the total volet count.
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name=row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add i to the lsit of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the % of votes for each candidate
for candidate_name in candidate_votes:
    # Get vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the % of votes.
    vote_percentage=float(votes)/float(total_votes) * 100
    
    # Determine if the votes is greaer than the winning count
    if (votes>winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count=votes and winning_percent =
        # vote_percentage
        winning_count=votes
        winning_percentage=vote_percentage
        # and, set the winning_candidate equal to the candidate's name
        winning_candidate=candidate_name
    # Print out each candidate's name, vote count and % of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n")
print(winning_candidate_summary)