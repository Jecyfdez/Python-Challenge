#import the os module and module to read csv files
import os
import csv

#store the file path associated with budget_data.csv across operating systems
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
col1 = []
col2 = []
months = []
total_months = 0
amount = 0
total_loss = 0
total_profit = 0

#open the file using csv module
with open(csvpath, newline='') as csvfile:
    #specify delimiter and variable "csvreader" that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #store a reference to a file stream
    #print(csvreader)
    #read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
          
    for row in csvreader:
        #Find the length of the list of months
        total_months = total_months + 1
        
        amount = int((row[1]))
       
        if amount >= 0:
            total_profit = total_profit + amount
           

        if amount < 0:
           total_loss = total_loss + amount

    print(f'Total Months: {total_months}')
    print(f'Profit: {total_profit}')
    print(f'Loss: {total_loss}')
   
    #The average of the changes in "Profit/Losses" over the entire period
    
    #The greatest increase in profits (date and amount) over the entire period
    
    
    #The greatest decrease in losses (date and amount) over the entire period


    #read each row of data after the header
   
        
