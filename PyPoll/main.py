import os
import csv

#create a path to open election_data.csv
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
    
    #Assign variables to outcomes wanted
c = {}
candidate_list = []
total_votes = 0
winner = 0

khan_votes = 0
khan_percent = 0

otooley_votes = 0
otooley_percent = 0

correy_votes = 0
correy_percent = 0

li_votes = 0
li_percent = 0

with open(csvpath, newline='') as csvfile:
    #specify delimiter and variable "csvreader" that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read the header row first
    csv_header = next(csvreader)
    
    #candidate_list = list(set(candidate_list))
    #candidates["name"]= candidate_list
        
    for row in csvreader:
        #The total number of votes cast
        total_votes = total_votes + 1
        name = row[2]
        candidate_list.append(name)
        
    for name in candidate_list:
        
        #COMPLETE LIST OF CANDIDATES AND NUMBER OF VOTES USING DICT()
        #c[name] = c.get(name,0) +1
        
        #candidate_list = list(set(candidate_list))
        
    #print(c)
        #assign candidate votes to a variable to print in proper text format
        #The total number of votes each candidate won
        #The percentage of votes each candidate won
        if name == "Khan":
            khan_votes += 1
            khan_percent = (khan_votes / total_votes)
            khan_percent= "{:.3%}".format(khan_percent)
             
        if name == "O'Tooley":
            otooley_votes += 1
            otooley_percent = (otooley_votes / total_votes)
            otooley_percent= "{:.3%}".format(otooley_percent)
             
        if name == "Correy":
            correy_votes += 1
            correy_percent = (correy_votes / correy_votes)
            correy_percent= "{:.3%}".format(correy_percent)
            
        if name == "Li":
            li_votes += 1
            li_percent = (li_votes / total_votes)
            li_percent= "{:.3%}".format(li_percent)
    
        #The winner of the election based on popular vote.
        


    print('Election Results')
    print('------------------------')
    print(f'Total Votes: {total_votes}')
    print('------------------------')
   
    print()
    print(f'{khan_votes} {otooley_votes} {correy_votes} {li_votes}')
    print('------------------------')
    print('Winner: (winner)')
    print('------------------------')



