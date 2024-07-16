import pandas as pd
from pathlib import Path
# Load the data
file_path = "PyPoll/Resources/election_data.csv"
data = pd.read_csv(file_path)
# Calculate the total number of votes cast
total_votes = data['Ballot ID'].nunique()

# A complete list of candidates who received votes
candidates = data['Candidate'].unique()

# Calculate the total number of votes each candidate won
vote_counts = data['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
vote_percentages = (vote_counts / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = vote_counts.idxmax()

# Prepare the results
results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate in candidates:
    results += f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})\n"

results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file_path = 'PyPoll/Analysis/election_results.txt'
with open(output_file_path, 'w') as file:
    file.write(results)

output_file_path
