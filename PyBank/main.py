#import the os module and module to read csv files
import os
import csv

#store the file path associated with budget_data.csv across operating systems
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

months = []
total_months = 0

amount = 0
loss = 0
profit = 0
total_amount = 0

prev_month= 0
monthly_change = 0
total_change = 0
average_change = 0

max_change = 0
min_change = 0

#open the file using csv module
with open(csvpath, newline='') as csvfile:
    #specify delimiter and variable "csvreader" that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    for i, row in enumerate(csvreader):
        #Find the total number of months in the data set
        total_months = total_months + 1
        
        #The total number of months included in the dataset
        amount = int((row[1]))
        
        #find total profit
        if amount >= 0:
            profit = profit + amount
                 
        #find total loss
        if amount < 0:
           loss = loss + amount
           
        #The net total amount of Profit/Losses
        total_amount = profit + loss
        
        
        #The average of the changes in "profit/losses over the months
        #monthly_change = amount - profit
        if i > 0:
            #First find Monthly Change
            monthly_change = amount - prev_month
            total_change = total_change + monthly_change
        #lock amount as previous month for next iteration
        prev_month = amount
        
        #The average of the changes in "Profit/Losses" over the entire period
        average_change = total_change / (total_months)

        #The greatest increase in profits (date and amount) over the entire period
        #Find MAX
        if max_change < monthly_change:
            max_change = monthly_change
            max_date = (row[0])
            
        #The greatest decrease in losses (date and amount) over the entire period
        #Find MIN
        if min_change > monthly_change:
            min_change = monthly_change
            min_date = (row[0])
            
    #print text in terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_amount}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_date} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})')

#export a text file 'analysis.txt' with the results
output_path = os.path.join('..', 'PyBank', 'analysis', 'analysis.txt')
with open(output_path, "w", newline='') as textfile:
    print('Financial Analysis', file=textfile)
    print('----------------------------', file=textfile)
    print(f'Total Months: {total_months}', file=textfile)
    print(f'Total: ${total_amount}', file=textfile)
    print(f'Average Change: ${average_change}', file=textfile)
    print(f'Greatest Increase in Profits: {max_date} (${max_change})', file=textfile)
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})', file=textfile)
    
    
   
        
