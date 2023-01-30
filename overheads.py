# import overhead csv
import csv


def highest_overhead():
    # "open" function is used to open the "cash-on-hand-usd.csv" in read mode and assign it to "file" variable
    with open('csv_reports/overheads-day-90.csv', 'r') as file:
        # csv.reader is used to create a reader object for the file
        reader = csv.reader(file)
        # Skips the header row of the csv file
        next(reader)

        categories = []
        overheads = []
        
        for category,overhead in reader:
            categories.append(category)
            overheads.append(float(overhead))
    highest_overhead_index = overheads.index(max(overheads))
    with open("summary_report.txt", "w") as txtfile:
        txtfile.write(f"[HIGHEST OVERHEADS] {categories[highest_overhead_index].upper()}: {overheads[highest_overhead_index]}%\n")