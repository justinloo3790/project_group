from cash_on_hand import *
from overheads import *
from profit_and_loss import *



with open("summary_report.txt", "w") as f:
    f.write("[HIGHEST OVERHEADS] {} EXPENSE: {}%\n".format(expense,expense_percentage))
    
    if cash_results == 0:

        for l in range (len(cash_deficit_amt)):
            f.write("[{0}] DAY: {1}, AMOUNT: USD{2}\n".format(cash_details,cash_deficit_day[l],cash_deficit_amt[l]))
    
    else:
        f.write("[{0}] CASH ON EACH DAY IS {1} THAN THE PREVIOUS DAY\n".format(cash_details,cash_results))

    if profit_results == 0:

        for m in range (len(profit_deficit_amt)):
            f.write("[{0}}] DAY: {1}, AMOUNT: USD{2}\n".format(profit_details,profit_deficit_day[m],profit_deficit_amt[m]))
    
    else:
        f.write("[{0}] NET PROFIT ON EACH DAY IS {1} THAN THE PREVIOUS DAY\n".format(profit_details,profit_results))
