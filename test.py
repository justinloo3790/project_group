# Import "csv" module to read the csv file
import csv

def coh():
    # "open" function is used to open the "cash-on-hand-usd.csv" in read mode and assign it to "file" variable
    with open('csv_reports/cash-on-hand-usd.csv', 'r') as file:
        # csv.reader is used to create a reader object for the file
        reader = csv.reader(file)
        # Skips the header row of the csv file
        next(reader)
    
        # An empty dictionary "data" is created to store data which is read from the csv file
        data = {}

        # Iterates rows in csv file containing days as first element and cash amount as second using for loop
        # "data" dictionary will store the day as key and cash amount as value, which is converted to int data taype
        for day, amt in reader:
            data[(day)] = int(amt)  

    # An empty dictionary "differences" is created which will store the day as key and deficit amount as value
    differences = {}
    # An empty string is created and assigned to the "previous_value" variable
    previous_value = ""

    # Iterates the items in "data" dictionary
    # If "previous_value" is not empty and "value" is less than "previous_value", "differences" will store the day as key and deficit amount as value
    for key, value in data.items():
        if previous_value != "" and value < previous_value:
            differences[key] = previous_value - value
        # Initializing by assigning the first value to "previous_value"
        previous_value = value

    # Iterates items in "differences" dictionary and prints a message
    with open("summary_report.txt", "a") as txtfile:
        for key, value in differences.items():
            txtfile.write(f"[CASH DEFICIT] DAY: {key}, AMOUNT: USD {value}\n")     
