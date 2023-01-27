import csv

def profit_loss():

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
                    profitandloss.append(value)

    profitandloss = []
    profit_results = 0
    profit_day = []
    profit_amt = []
    profit_details = 0
    profit_deficit_day = []
    profit_deficit_amt = []





    #type ur code here bro jiayous ;> add any variables if u want






    with open("summary_report.txt", "w") as f:
        
        if profit_results == 0:

            for m in range (len(profit_deficit_amt)):
                f.write("[{0}}] DAY: {1}, AMOUNT: USD {2}\n".format(profit_details,profit_deficit_day[m],profit_deficit_amt[m]))
        
        else:
            f.write("[{0}] NET PROFIT ON EACH DAY IS {1} THAN THE PREVIOUS DAY\n".format(profit_details,profit_results))