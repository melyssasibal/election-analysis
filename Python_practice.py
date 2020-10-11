voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson", "registered_voters":432438}]
for county_dict in voting.data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")


#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a test file
with open(file_to_save, "w") as txt_file:
    #Write three counties to the file 
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")