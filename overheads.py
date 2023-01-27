import csv

def overheads():

    # create empty lists to store the category and overheads 
    expense = []
    expense_percentage = 0
    expense_type = []
    expense_amt = []

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


    

    # append the category and overheads as a list back into the empty list respectivetly
    for n in range(1,len(expense),2):
        print(expense[n])
        for o in range (n+2,len(expense),2):
            print(expense[o])
            if float(expense[n]) > float(expense[o]):
                expense_amt.append(expense[n])
            else:
                break

    print(expense_amt)


    # with open("summary_report.txt", "w") as f:
    #     f.write("[HIGHEST OVERHEADS] {} EXPENSE: {}%\n".format(expense_type,expense_percentage))

overheads()
