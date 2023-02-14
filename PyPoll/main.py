#  Declaring our variables
header_row = ''
temp_data = {}
csv_data = {}
candidate = ''
candidate_list = []
all_candidates = {
    "name": 0,
    "count": 0,
}
vote_sum = 0

# The total number of votes cast
# A complete list of candidates who received votes - The percentage of votes each candidate won% - (The total number of votes each candidate won)
# The winner of the election based on popular vote

# Importing the CSV file 
with open('resources/election_data.csv', 'r') as file:
    lines = file.read().split('\n')

# Creating a header from Line 1 in the CSV file
header_row = lines[0].split(',')

# Using a for loop to loop through the CSV lines and copy them to a dictionary, in sequential order
for line in range(1, len(lines)):
    data_line = lines[line].split(',')
    temp_data = dict(zip(header_row, data_line))
    csv_data[line] = temp_data


# Printing the total number of votes. Subtracting 1 for the header row, and 1 for an empty line at the end of the CSV
print(f'Total Votes: ' + str(len(lines) - 2))


# Using a for loop to go through the dictionary and add the names onto a list; Removing the last line because it is empty
for i in range(1, len(lines)):
    if csv_data[i].get("Candidate") != candidate and csv_data[i].get("Candidate") != None:
        candidate = csv_data[i].get("Candidate")
        candidate_list.append(candidate)
print(candidate_list)



# Loop through the candidate list for a name, then count how many votes that name got in the dictionary
for name in candidate_list:
    for i in range(1, len(lines)):
        if csv_data[i].get("Candidate") == candidate:
            vote_sum += 1
    vote_sum = 0
 
