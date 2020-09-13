# Add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Candidate options and candidate votes
candidate_options = []
candidate_votes ={}

county_list = []
county_dict = {}



#Track the winning candidate, vote count, and percentage.
winning_candidate =""
winning_count = 0
Winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load)as election_data:
    file_reader = csv.reader(election_data)

#Print the header row    
    headers = next(file_reader)

#Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count. 
        total_votes = total_votes + 1
        #Get the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]

        if county_name not in county_list:
            county_list.append(county_name)
            county_list[county_name] = 0
            county_list[county_name] = county_list[county_name] + 1

            for county_name in county_list
            print(county name)



        #If the candidate does not match any existing candidate, add it to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate's name to the candidate list.
            candidate_options.append(candidate_name)
            #And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        #Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    election_results =(
   f"\nElection Results\n"
   f"-------------------\n"
   f"Total Votes:  {total_votes:,}\n"
   f"----------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file.
    txt_file.write(election_results)

   