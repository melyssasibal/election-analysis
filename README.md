# Election Analysis 

## Overview of Project 
The purpose of this analysis was to complete an audit of a recent local congressional election. The election data was found to be comprised of 369,711 votes across three counties in Colorado: Jefferson, Denver and Arapahoe. Analysis was done using Python. 

To complete the audit, the following was done: 
- Calculate the total number of votes cast. 
- Get a complete list of candidates who received votes. 
- Calculate the total number of votes each candidate received. 
- Calculate the percentage of votes each candidate won. 
- Determine the winner of the election based on popular vote. 

## Election-Audit Results
The audit of the election shows that: 
- A total of 369,711 votes were found to be cast in this congressional election. 
- The calculated breakdown of votes across each county:
    - Jefferson: 10.5% (38,855 votes)
    - Denver:82.8% (306,055 votes)
    - Arapahoe: 6.7% (24,801 votes)
- Denver was calculated to have the largest number of votes. 
- The calculated breakdown of votes each candidate received:
    - Charles Casper Stockham: 23.0% (85,213 votes)
    - Diana DeGette: 73.8% (272,892 votes)
    - Raymon Anthony Doane: 3.1% (11,606 votes)
- Diana DeGette won the popular vote with 73.8% of total votes (272,892 votes)

## Election-Audit Summary 
Continued used of this script could be helpful in automating analysis of future elections. Some modification would be required before applying the script to results of another elections. Examples include: 
- Editing the file paths for the dataset file and analysis file
- Specifying how votes will be disaggregated (if data included sex, age, political party, other geopgraphic locations, etc., script could be edited to run analysis for specified stratifications)
- Editing index within row of dataset to return candidate name/county name/specified stratification
- Modifying printed results to reflect analysis as desired