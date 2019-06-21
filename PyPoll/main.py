#Application to update poll data

#First import path and csv
import os
import csv

# set path for input file
# data directory is two levels below program location
electioncsv = os.path.join("..", "PyPoll", "election_data.csv")

# set path for output file
outputfile = os.path.join("..", "PyPoll", "Election_Summary.txt")

#Set variable for Total votes euqal to 0
# store total votes in dictionary
total_votes=0
results={}

with open(electioncsv,'r') as csvfile:
    # split the data
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the headers
    next(csvreader)

    # loop through the data
    for row in csvreader:

        # put candidate name into variable
        candidate=str(row[2])

        # make dictionary from candidate name, value = votes
        if candidate in results:
            results[candidate] = results[candidate]+1   
        else:
            results[candidate] = 1
#define the winner based on amount of results
winner = max(results, key=results.get)

# print to terminal
print("Election Results")
print("________________________________________________")
print("Total Votes: " + str(sum(results.values() )))
print("________________________________________________")

for key in results:
    print (key + ": " + str(  round( (results[key]/sum(results.values() ))*100 , 3 )  ) + "% (" + str(results[key]) + ")")

print("________________________________________________")
print(f"Winner: {winner}")
print("________________________________________________")

# print to file
with open(outputfile,"w") as file:
    file.write("Election Results\n")
    file.write("\n-------------------------\n")
    file.write("Total Votes: " + str(sum(results.values())))
    file.write("\n-------------------------\n")

    for key in results:
        file.write(key + ": " + str(round((results[key]/sum(results.values())) * 100 , 3 )) + "% (" + str(results[key]) + ")")
        file.write("\n-------------------------\n")
        file.write(f"Winner: {winner}")
        file.write("\n-------------------------\n")