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

    #Create nested loop to access each value in the list and append the value to the 'cashonhand' list.
        for line in reader:
                for value in line:
                    cashonhand.append(value)


    #The 'k' in the for loop represents the position of the value in the list. 
    #The loop starts from 1 and ends at 21 and it only takes the odd numbered positions in the list which is the amount on each day.
    for k in range(1,len(cashonhand)-1,2):

        #If the current day is more than the previous day, meant that the current day amount is more than the previous day amount.
        if float(cashonhand[k+2]) > float(cashonhand[k]):

            #since current is more than previous it will be recorded and it will collate the total number of days that are more than its previous day
            number_of_surplus+=1

        #If its less than the previous day, the shortaged amount and its day will be added into a list respectiviely.
        elif int(cashonhand[k+2]) <= int(cashonhand[k]):

            cash_deficit_amt.append(int(cashonhand[k]) - int(cashonhand[k+2]))

            cash_deficit_day.append(cashonhand[k+1])

    #The if else will summarise the results and determine whether if all of the days were more or less than the previous 
    #if its neither, it has an mixed number of shortages and surplus then it will be categorised as cash deficit
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

#To print the cash on hand out
coh()