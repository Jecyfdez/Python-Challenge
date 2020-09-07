import os
import csv

csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')

c ={}
khan = 0
correy = 0
li = 0
otooley = 0
total_votes = 0

with open(csvpath, newline='') as csvfile:
#specify delimiter and variable "csvreader" that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #store a reference to a file stream
    #print(csvreader)
    #read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #candidate_list = list(set(candidate_list))
    #candidates["name"]= candidate_list
        
    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] == "Khan":
            khan = khan +1
        #if row[2] == Correy:
            #correy= correy + 1
            
            

    #candidates = {"name":"Khan","Correy","Li","O'Tooley"}

    #The percentage of votes each candidate won

    #The total number of votes each candidate won

    #The winner of the election based on popular vote.

    print('Election Results')
    print('------------------------')
    print(f'Total Votes: {total_votes}')
    print('------------------------')
    print(f'Khan: ({khan})')
    print()
    print('------------------------')
    print('Winner:')
    print('------------------------')

