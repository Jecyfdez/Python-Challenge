#import the os module and module to read csv files
import os
import csv

#store the file path associated with budget_data.csv across operating systems
csvpath = os.path.join('..','Resources','budget_data.csv')

#open the file using csv module
with open(csvpath, newline="") as csvfile:
    #specify delimiter and variable "csvreader" that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #store a reference to a file stream
    print(csvreader)
    
    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #read each row of data after the header
    for row in csvreader:
        print(row)
        
    
    
    
