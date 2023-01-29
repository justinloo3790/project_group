# import overhead csv
import csv

name = 0
amount = 0

def overheads():

    expense = []
    
    with open('csv_reports/overheads-day-90.csv', "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        for line in reader:
             for value in line:
                  expense.append(value)
                  
    for i in range(0,len(expense),2):
        for x in range(0,len(expense),2):
           if float(expense[i+1]) >= amount:
            name, amount = expense[i], float(expense[i+1])
           else:
               break

with open("summary_report.txt", "w") as reportFile:
        reportFile.write(f'[HIGHEST OVERHEADS] {name}: {amount}%')