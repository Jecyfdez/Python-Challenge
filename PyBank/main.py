#import the os module and module to read csv files
import os
import csv

#store the file path associated with budget_data.csv across operating systems
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

#open the file using csv module
with open(csvpath) as csvfile:
    #specify delimiter and variable "csvreader" that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #store a reference to a file stream
    print(csvreader)
    
    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Find total number of months included in the data
    ##TOTAL MONTHS
    total_months = len(list(csvreader))
    print(f'Total Months: {total_months}')
    
    #The net total amount of "Profit/Losses" over the entire period
    
    
    #The average of the changes in "Profit/Losses" over the entire period
    
    #The greatest increase in profits (date and amount) over the entire period
    
    
    #The greatest decrease in losses (date and amount) over the entire period


    #read each row of data after the header
    for row in csvreader:
        print(row)
          

