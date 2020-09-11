#   The data we need to retrieve.
#   1.  The total number of votes cast
#   2.  A complete list of candidates who received votes
#   3.  The percentage of votes each candidate won
#   4.  The total number of votes each candidate won
#   5.  The winner of the election based on popular vote.
import csv
import os
#   Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

#Candidate Options and candidate votes
candidate_options = []

#   1.Declare the empty dictionary.
candidate_votes = {}

#Open the election results and read the file
with open(file_to_load) as election_data:

#   To do: perform analysis
    file_reader = csv.reader(election_data)
    
    #   Read the header row
    headers = next(file_reader)
    
     #Print each row in the CSV file
    for row in file_reader:
        total_votes = total_votes + 1
   
   
    #   print the candidate name from each row
        candidate_name = row[2]

    #   If the candidate does not match any existing candidate..
        if candidate_name not in candidate_options:
        

    # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

    #   2.  Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] =0

    #   Add a vote to that candidate's count
    #     candidate_votes[candidate_name] +=1


    #   print the candidate vote dictionary.
    print(candidate_votes)
        
        
   
#   Close the file
#outfile.close()
