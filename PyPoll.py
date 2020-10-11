#The data we need to retrieve
#1. The total number of votes cast 
#2. A complete list of candidates who received votes 
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won 
#5. The winner of the election based on popular vote

#Add dependencies
import csv
import os 

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a test file
with open(file_to_save, "w") as txt_file:
    #Write three counties to the file 
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    
#Assign a variable for the file to load and the path
file_to_load = os.path.join('election_results.csv')

#Initialize a total vote counter
total_votes = 0 

#Declare candidate list
candidate_options = []

#Declare candidate votes dictionary
candidate_votes = {}

#Declare winning candidate string and winning count tracker 
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
     
    #Read the file object with the reader function 
    file_reader = csv.reader(election_data)

    #Print the header row. 
    headers = next(file_reader)
    
    #Print each row in CSV file
    for row in file_reader: 
        #Add to the total vote count
        total_votes += 1 

        #Print the candidate name from each row 
        candidate_name = row[2]

        #If candidate_name is not already in candidate_options
        if candidate_name not in candidate_options:
            #Then, add to list 
            candidate_options.append(candidate_name)

            #Track candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add to candidate votes
        candidate_votes[candidate_name] += 1

#Print the total votes
#print(f"{total_votes:,}")

#Print the candidate list 
#print(candidate_options)

#Print candidate vote dictionary
#print(candidate_votes)

#Determine percentage of votes for each candidate by looping through counts
#Iterate through candidate_options list 
for candidate_name in candidate_votes:
    #Retrieve vote count of each candidate
    votes = candidate_votes[candidate_name]
    #Calculate percentate 
    vote_percentage = float(votes) / float(total_votes) *100 
    #Print candidate name and percentage of votes 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count, percentage and candidate 
    #Determine if votes are greater than winning count and percentage
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true, then set winning_count to votes and winning_percentage to vote_percentage 
        winning_count = votes
        winning_percentage = vote_percentage 
        #Set winning_candidate equal to candidate's name 
        winning_candidate = candidate_name

#Print winning candidate, vote count and percentage 
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n"
)
print(winning_candidate_summary)