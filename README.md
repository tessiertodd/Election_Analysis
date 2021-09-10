# Election_Analysis

## Project Overview
Two Board of Elections employees (Tom & Seth) are looking for some help to calculate some of the key metrics from the election results.
Original project was to calculate total votes, list of candidates with votes, votes for each candidate and determine who the winner was.
The Challenge was an additional ask to have a little more information... here are the pieces of additional information that were requested:
1) Calculate the breakdown of votes by county.
2) Idenfity which county had the highest number of votes.
3) Also include information from original project - total votes, candidate names, candidate votes/% and declare election winner.

## Resources
- Data Source: election_results.csv
- Sofware: Python 3.6.7, Visual Studio Code 1.60.0

## Summary
The analysis shows the following:
- There were 369,711 votes cast in the election.

![Table for total votes](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/Total%20Election%20Results.png)

- County names where voting took place, % votes of each and number of votes
  - Jefferson had 10.5% of votes (38,855 votes)
  - Denver had 82.8% of votes (306,055 votes)
  - Arapahoe had 6.7% of votes (24,801 votes)
 - Denver was the county with the most votes at 82.8%
 
 Code to print out the winning county and snippet of printout:
 ![Table Winning County Code](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/Winning%20County%20code.png)
 
 ![Table Winning County](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/Winning%20County.png)
    
  Here is a view of the code used to count the votes by county and then code to print out and save to text file:
 ![Table_County_Names_Count](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/County%20Votes%20-%20counting%20code.png)
 ![Table County Codes Count](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/County%20Votes%20code.png)
  
- Candidate names, % of total votes each had and number of votes
  - Charles Casper Stockham 23.0% of votes (85,213 votes)
  - Diana DeGette 73.8% of votes (272,892 votes)
  - Raymon Anthony Doane 3.1% of votes (11,606 votes)

![Table Candidate Names](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/Candidate%20names.png) 

- The election winner is:
  - Diana DeGette with 73.8% of votes (272,892 votes)

![Table Winning Candidate](https://github.com/tessiertodd/Election_Analysis/blob/main/Resources/Winning%20Candidate.png)

## Challenge Overview
Election Board needed some information beyond the information by candidate they had already received.  They wanted to better understand voter split % by county and vote counts.

## Challenge Summary
Denver had the largest number of voters out of the total voters by a significant percentage with 82.8% (306,055) of the votes coming from that county.
Jefferson county had 10.5% of voters (38,855) and Arapahoe had 6.7% (24,801).

Diana DeGette was the winning candidate who had 272,982 votes which was 73.8% of the total votes.

An additional piece of information that would be helpful would be if we have the number of eligible voters in each county.  With this additional information, we could calculate the % of voter turnout vs. eligible voters which may show which counties had the best voter turnout.  This information may help the Election Board in future elections help push in the right counties to increase the voter turnout for future elections.

## Election-Audit Summary:
This script has been setup in such a way that we could adapt for other elections.  We could use this same code to analyze election information where there are 10 candidates and 20 counties. Given the approach to setting up lists and dictionaries without defining a specific number, we can have data with any number of candidates and/or counties without us needing to adjust the code.

If the data also contained Postal Codes for example, we could add code like we did for the counties for postal codes to get a sense of how many votes were cast in these smaller geographic regions. Ideally we could leverage dictionaries within dictionaries to understand the voting split between postal codes within a county. Again, if we had eligible voter numbers by county and postal code that would help you understand where voter turnout might be low.

We could also leverage the ability to build dictionaries within dictionaries to build code to provide understanding on % of people (and number) who voted for each candidate within each county.  This would help you better understand where support for certain candidates lies between the counties. 
