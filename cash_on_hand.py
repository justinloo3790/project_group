# Import csv module
import csv

def coh():
    #Lists and variables
    cashonhand = []
    cash_deficit_day = []
    cash_deficit_amt = []
    cash_results = 0
    cash_details = 0
    number_of_surplus = 0

    #Creating file path for the excel
    with open('csv_reports/cash-on-hand-usd.csv', 'r') as file:

        # instantiate a reader object
        reader = csv.reader(file)
        # use `next()` to skip the header.
        next(reader)

    # Create nested loop to access each value in the list
    # and append the value to the dict.
        for line in reader:
                for value in line:
                    cashonhand.append(value)

    #Calculate which amount is more or less than the previous cash_day
    for k in range(1,len(cashonhand)-1,2):
        if float(cashonhand[k+2]) - float(cashonhand[k]) > 0:
            number_of_surplus+=1

        #If its less than the previous day, the differentiated amount and the day it falls on will be added into a list
        if float(cashonhand[k+2]) - float(cashonhand[k]) <= 0:
            cash_deficit_day.append(cashonhand[k+1])
            cash_deficit_amt.append(abs(int(cashonhand[k+2]) - int(cashonhand[k])))

    #The summary of the results will be compared to each other using the if else
    #to determine whether the surplus cash is higher or lower and if its mixed then it will be referred to as deficit
    if number_of_surplus == len(cashonhand)/2:
        cash_results = "HIGHER"
        cash_details = "CASH SURPLUS"

    elif number_of_surplus == 0:
        cash_results = "LOWER"
        cash_details = "CASH SHORTAGE"

    else:
        cash_details = "CASH DEFICIT"

    #Iterates items in the list and prints a message showing details of the 
    #whether it is cash surplus, cash shortage or cash deficit with the amounts and day.
    with open("summary_report.txt", "a") as f:

        if cash_results == 0:

            for l in range (len(cash_deficit_amt)):
                f.write("[{0}] DAY: {1}, AMOUNT: USD {2}\n".format(cash_details,cash_deficit_day[l],cash_deficit_amt[l]))
        
        else:
            f.write("[{0}] CASH ON EACH DAY IS {1} THAN THE PREVIOUS DAY\n".format(cash_details,cash_results))
        
        


