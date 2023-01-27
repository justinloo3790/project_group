import csv

def overheads():

    # create empty lists to store the category and overheads 
    expense = []
    expense_percentage = 0
    type_of_expense = []
    expenses_amt = []

    #Creating file path for the excel
    with open('csv_reports/overheads-day-90.csv', 'r') as file:

        # instantiate a reader object
        reader = csv.reader(file)
        # use `next()` to skip the header.
        next(reader)


    # Create nested loop to access each value in the list
    # and append the value to the dict.
        for line in reader:
                for value in line:
                    expense.append(value)

    print(expense)

    

    # append the category and overheads as a list back into the empty list respectivetly
    for expense in reader:
        if expense[0] == "type_of_expense":
            type_of_expense.append(expense[0])
        else:
            value.append(expense[1])


    with open("summary_report.txt", "w") as f:
        f.write("[HIGHEST OVERHEADS] {} EXPENSE: {}%\n".format(expense,expense_percentage))
