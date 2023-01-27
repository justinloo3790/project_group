# 1.Import Path function from pathlib 
from pathlib import Path
# Import csv module
import csv

#Lists and variables
cashonhand = []
cash_deficit_day = []
cash_deficit_amt = []
cash_day = [40,41,42,43,44,45,46,47,48,49,50]
cash_amt = [252049,40978,158019,250235,36039,36176,162363,130695,525331,26248,71961]
cash_results = 0
cash_details = 0
number_of_surplus = 0


# #Creating file path for the excel
# file_path = Path.home()/"Documents"/"GitHub"/"project_group"/"cash-on-hand-usd.csv"

# # create 'reader' object and print line if file path exists
# with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:

#     # instantiate a reader object
#     reader = csv.reader(file)
#     # use `next()` to skip the header.
#     next(reader)


# # Create nested loop to access each value in the list
# # and append the value to the dict.
#     for line in reader:
#             for value in line:
#                 cashonhand.append(value)

print(len(cashonhand))
#Add all the cash_days into a list
for i in range(0,len(cashonhand),2):
    cash_day.append(cashonhand[i])

#Add all the amounts for each cash_day into a list
for j in range(1,len(cashonhand),2):
    cash_amt.append(cashonhand[j])



#Calculate which amount is more or less than the previous cash_day
for k in range(0,len(cash_amt)-1,1):
    if float(cash_amt[k+1]) - float(cash_amt[k]) > 0:
        number_of_surplus+=1

    #If its less than the previous day, the lesser amount and the day it falls on will be added into a listS
    if float(cash_amt[k+1]) - float(cash_amt[k]) <= 0:
        cash_deficit_day.append(cash_day[k+1])
        cash_deficit_amt.append(cash_amt[k+1])



#The summary of the results will be compared to each other using the if else
#to determine whether the surplus cash is higher or lower and if its mixed then it will be referred to as deficit
if number_of_surplus == len(cash_amt):
    cash_results = "HIGHER"
    cash_details = "CASH SURPLUS"

elif number_of_surplus == 0:
    cash_results = "LOWER"
    cash_details = "CASH SHORTAGE"

else:
    cash_details = "CASH DEFICIT"



