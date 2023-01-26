expense = 0
expense_percentage = 0

# create a filepath for the csv file 
filepath = Path.cwd()/"Documents"/"GitHub"/"project_group"/"overheads-day-90.csv"
# read the csv file to append category and overheads from csv
with filepath.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    
    from pathlib import Path
    import csv

# create 2 empty lists to store the category and overheads 
type_of_expense = []
value = []
# append the category and overheads as a list back into the empty list respectivetly
for expense in reader:
    if expense[0] == "type_of_expense":
        type_of_expense.append(expense[0])
    else:
        value.append(expense[1])

