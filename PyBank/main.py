import os
import csv

file_path = os.path.join('/Users/daryarudych/Desktop/repos/python-challenge/PyBank','budget_data.csv')
print(file_path)

with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)
    date, revenue = zip(*csvreader)
    
#Calculating the number of months 
print(f"Total months: {len(date)}")

#Offsetting a list of dates by -1 to match the change list 
new_date = date[1:]

#Converting a string list to a float list  
new_revenue = []
new_revenue = [ float(x) for x in revenue ]
print(new_revenue)

#Calculating the net profit
print(f"Net Profit: {sum(new_revenue)}")

#Calculating the average change in "Profit/Losses" between months over the entire period

#1 - combine list of revenue values with itself offsetting by 1. Creates pairs of values to be subtracted

change_list = [x-y for x, y in zip(new_revenue[1:], new_revenue)]    
print(change_list) 

#2 - see how many values in the list
len(change_list)

#3 - create a function that calculates the average profit

average = sum(change_list)/len(change_list)
print(f"Average change: {average}")


#Printing out the summary 
print ("Financial Analysis Summary:")
print(f"Total months: {len(date)}")
print(f"Net Profit: {sum(new_revenue)}")
print(f"Average change: {average}")
print(f"Greatest increase in profits: {new_date[change_list.index(max(change_list))]} {max(change_list)}")
print(f"Greatest decrease in Profits: {new_date[change_list.index(min(change_list))]} {min(change_list)}")
    