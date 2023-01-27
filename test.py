# import csv

# #This is to open the "cash-on-hand-usd.csv" file in read mode, and the file object is then assigned to the "file" variable
# with open('cash-on-hand-usd.csv', 'r') as file:
#     #This is to read the file object and assign it to the "reader" variable
#     reader = csv.reader(file)
#     #This is to skip the first line of the .csv file which contains the headers
#     next(reader)
#     #This is to assign an empty string to the variable "previous_day"
#     previous_day = ""
#     #This is to assign the value 0 to the "total_amt" variable which will later store the total cash amount for each day
#     total_amt = 0
#     #This is to assign an empty dictionary to the "day_amt" which will later store the day number and the total amount for that day
#     day_amt = {}
#     #This is to create a for loop which will iterate each row in the .csv file, extracting the date and 
#     for row in reader:
#         #This is to get the day on the .csv file using index position 0, which will be changed to integer data type and assigned to the "current_day" variable
#         current_day = int(row[0])
#         #This is to get the cash amount on the .csv file using index position 3, which will be changed to float data type and assigned to the "amount" variable
#         amount = float(row[3])
#         #This will execute lines 23 to 26 if the condition that the current_day is the same as the previous_day
#         if current_day == previous_day:
#             #This is to update the "total_amt" variable by adding the the amount in the current loop
#             total_amt += amount
#             #This is to update the day_amt dictionary with the current day as the key and the total amount as the value
#             day_amt[(current_day)] = total_amt
#         #This is to execute lines 29 to 34 if the condition that the current day is the same as the previous day is not met
#         else:
#             #This is to reset the "total_amt" variable with the cash amount of the first transaction in a new day
#             total_amt = amount
#             #This is to update the variable "previous_day" to the current day
#             previous_day = current_day
#             #This is to update the "day_amt" dictionary with the current_day as the key and the new total amount as the value
#             day_amt[(current_day)] = total_amt
# print(day_amt)
# #store_amt = 0
# #sorted_day_amt = dict(sorted(day_amt.items()))
# #for day, amt in sorted_day_amt.items():
#     #print(day, amt)

import csv

cashonhand = []
cash_deficit_day = []
cash_deficit_amt = []
cash_day = []
cash_amt = []
cash_results = 0
cash_details = 0
number_of_surplus = 0

with open('cash-on-hand-usd.csv', 'r') as file:

    reader = csv.reader(file)

    next(reader)


# Create nested loop to access each value in the list
# and append the value to the dict.
    for line in reader:
            for value in line:
                cashonhand.append(value)

print(cashonhand)

#Add all the cash_days into a list
for i in range(0,len(cashonhand),4):
    cash_day.append(cashonhand[i])

#Add all the amounts for each cash_day into a list
for j in range(3,len(cashonhand),4):
    cash_amt.append(cashonhand[j])

print(cash_day)
print(cash_amt)

# #Calculate which amount is more or less than the previous cash_day
# for k in range(0,len(cash_amt)-1,1):
#     if float(cash_amt[k+1]) - float(cash_amt[k]) > 0:
#         number_of_surplus+=1

#     #If its less than the previous day, the lesser amount and the day it falls on will be added into a listS
#     if float(cash_amt[k+1]) - float(cash_amt[k]) <= 0:
#         cash_deficit_day.append(cash_day[k+1])
#         cash_deficit_amt.append(cash_amt[k+1])



# #The summary of the results will be compared to each other using the if else
# #to determine whether the surplus cash is higher or lower and if its mixed then it will be referred to as deficit
# if number_of_surplus == len(cash_amt):
#     cash_results = "HIGHER"
#     cash_details = "CASH SURPLUS"

# elif number_of_surplus == 0:
#     cash_results = "LOWER"
#     cash_details = "CASH SHORTAGE"

# else:
#     cash_details = "CASH DEFICIT"