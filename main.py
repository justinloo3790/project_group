from cash_on_hand import *
from overheads import *
from profit_and_loss import *


def main():
    coh()
    #profit_loss()

main()

# import overhead csv
import csv


def overheadsTest():
    # "open" function is used to open the "cash-on-hand-usd.csv" in read mode and assign it to "file" variable
    with open('csv_reports/overheads-day-90.csv', 'r') as file:
        # csv.reader is used to create a reader object for the file
        reader = csv.reader(file)
        # Skips the header row of the csv file
        next(reader)

        #
        cat_overheads = {}

        # Iterates rows in csv file containing days as first element and cash amount as second using for loop
        # "data" dictionary will store the day as key and cash amount as value, which is converted to int data taype
        for category, oh in reader:
            cat_overheads[(category)] = oh

    highest_overhead = ""
    previous_overhead = ""
    for category,overhead in cat_overheads.items():
        for higher_overhead in cat_overheads:
         if overhead != "" and previous_overhead < overhead:
            continue
         else:
            break
        previous_overhead = overhead
    return overhead


print(overheadsTest())