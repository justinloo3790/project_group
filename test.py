import csv

#This is to open the "cash-on-hand-usd.csv" file in read mode, and the file object is then assigned to the "file" variable
with open('cash-on-hand-usd.csv', 'r') as file:
    #This is to read the file object and assign it to the "reader" variable
    reader = csv.reader(file)
    #This is to skip the first line of the .csv file which contains the headers
    next(reader)
    #This is to assign an empty string to the variable "previous_day"
    previous_day = ""
    #This is to assign the value 0 to the "total_amt" variable which will later store the total cash amount for each day
    total_amt = 0
    #This is to assign an empty dictionary to the "day_amt" which will later store the day number and the total amount for that day
    day_amt = {}
    #This is to create a for loop which will iterate each row in the .csv file, extracting the date and 
    for row in reader:
        #This is to get the day on the .csv file using index position 0, which will be changed to integer data type and assigned to the "current_day" variable
        current_day = int(row[0])
        #This is to get the cash amount on the .csv file using index position 3, which will be changed to float data type and assigned to the "amount" variable
        amount = float(row[3])
        #This will execute lines 23 to 26 if the condition that the current_day is the same as the previous_day
        if current_day == previous_day:
            #This is to update the "total_amt" variable by adding the the amount in the current loop
            total_amt += amount
            #This is to update the day_amt dictionary with the current day as the key and the total amount as the value
            day_amt[(current_day)] = total_amt
        #This is to execute lines 29 to 34 if the condition that the current day is the same as the previous day is not met
        else:
            #This is to reset the "total_amt" variable with the cash amount of the first transaction in a new day
            total_amt = amount
            #This is to update the variable "previous_day" to the current day
            previous_day = current_day
            #This is to update the "day_amt" dictionary with the current_day as the key and the new total amount as the value
            day_amt[(current_day)] = total_amt
print(day_amt)
#store_amt = 0
#sorted_day_amt = dict(sorted(day_amt.items()))
#for day, amt in sorted_day_amt.items():
    #print(day, amt)



