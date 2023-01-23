# 1.Import Path function from pathlib 
from pathlib import Path
# Import csv module
import csv

#Lists and variables
cashonhand = []
day = []
amt = []
cash_surplus = 0
More_than = 0
Less_than = 0

#Creating file path for the excel
file_path = Path.home()/"Documents"/"GitHub"/"project_group"/"cash-on-hand-usd.csv"

# create 'reader' object and print line if file path exists
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:

    # instantiate a reader object
    reader = csv.reader(file)
    # use `next()` to skip the header.
    next(reader)


# Create nested loop to access each value in the list
# and append the value to the dict.
    for line in reader:
            for value in line:
                cashonhand.append(value)


#Add all the days into a list
for i in range(0,len(cashonhand),2):
    day.append(cashonhand[i])

#Add all the amounts for each day into a list
for j in range(1,len(cashonhand),2):
    amt.append(cashonhand[j])

def scenario1_cashonhand(amt,More_than,Less_than,cash_surplus):
    #Calculate which amount is more or less than the previous day and then compiling it into two variables
    for k in range(0,len(amt)-1,1):
        if float(amt[k+1]) - float(amt[k]) > 0:
            More_than+=1
        else:
            Less_than+=1

    #The summary of the complilation of the results will be compared to each other using the if else and return function
    #to determine whether the surplus cash is higher or lower as a whole 
    if More_than >= Less_than:
        cash_surplus = "HIGHER"
    else:
        cash_surplus = "LOWER"
    
    return cash_surplus

#To start the function and return the cash_surplus results
cash_surplus = scenario1_cashonhand(amt,More_than,Less_than,cash_surplus)

def scenario2_cashonhand(amt,More_than,Less_than,cash_surplus):
    #Calculate which amount is more or less than the previous day and then compiling it into two variables
    for k in range(0,len(amt)-1,1):
        if float(amt[k+1]) - float(amt[k]) > 0:
            More_than+=1
        else:
            Less_than+=1

    #The summary of the complilation of the results will be compared to each other 
    #to determine whether the surplus cash is higher or lower in general
    if More_than >= Less_than:
        cash_surplus = "HIGHER"
    else:
        cash_surplus = "LOWER"
    
    return cash_surplus