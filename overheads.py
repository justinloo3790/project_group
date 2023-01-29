# import overhead csv
import csv

def overheads():

    # create empty lists to store the category and overheads 
    expense = []
    expense_percent = 0
    expense_type = 0

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

    # append the category and overheads as a list back into the empty list respectively
    for n in range(1,len(expense),2):
        for o in range (1,len(expense),2):
            if float(expense[n]) > float(expense[o]):
                expense_percent = expense[n]
                expense_type = expense[n-1]
            else:
                break
    

    with open("summary_report.txt", "w") as f:
        f.write("[HIGHEST OVERHEADS] {}: {}%\n".format(expense_type.upper(),expense_percent))