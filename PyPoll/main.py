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
        c[name] = c.get(name,0) +1
        
        candidate_list = list(set(candidate_list))
    
    #FIND THE TOTAL NUMBER VOTES PER CANDIDATE
    #FIND THE PERCENTAGE OF VOTES
    #FORMAT TO PERCENTAGE WITH 3 DECIMALS

    khan_votes = (c["Khan"])
    khan_percent = khan_votes/total_votes
    khan_percent= "{:.3%}".format(khan_percent)
    
    correy_votes = (c["Correy"])
    correy_percent = correy_votes/total_votes
    correy_percent= "{:.3%}".format(correy_percent)
    
    li_votes = (c["Li"])
    li_percent = li_votes / total_votes
    li_percent = "{:.3%}".format(li_percent)
    
    otooley_votes = (c["O'Tooley"])
    otooley_percent = otooley_votes / total_votes
    otooley_percent= "{:.3%}".format(otooley_percent)
            

    
 
print('Election Results')
print('------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------')
print(f'Khan: {khan_percent} ({khan_votes})')
print(f'Correy: {correy_percent} ({correy_votes})')
print(f'Li: {li_percent} ({li_votes})')
print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
print('------------------------')
print('Winner: Khan')
print('------------------------')



output_path = os.path.join('..', 'PyPoll', 'analysis', 'analysis.txt')
with open(output_path, "w", newline='') as textfile:
    print('Election Results', file=textfile)
    print('------------------------', file=textfile)
    print(f'Total Votes: {total_votes}', file=textfile)
    print('------------------------', file=textfile)
    print(f'Khan: {khan_percent} ({khan_votes})', file=textfile)
    print(f'Correy: {correy_percent} ({correy_votes})', file=textfile)
    print(f'Li: {li_percent} ({li_votes})', file=textfile)
    print(f"O'Tooley: {otooley_percent} ({otooley_votes})", file=textfile)
    print('------------------------', file=textfile)
    print('Winner: Khan', file=textfile)
    print('------------------------', file=textfile)


