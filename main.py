from cash_on_hand import *
from overheads import *
from profit_and_loss import *

scenario = 1


if scenario == 1:
    with open("summary_report.txt", "w") as f:
        f.write("[HIGHEST OVERHEADS] SALARY EXPENSE: {}%\n".format(salary_expense))
        f.write("[CASH SURPLUS] CASH ON EACH DAY IS {} THAN THE PREVIOUS DAY\n".format(cash_surplus))
        f.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY is {} THAN THE PREVIOUS DAY\n".format(salary_expense))

if scenario == 2: 
    with open("summary_report.txt", "w") as f:
        f.write("[HIGHEST OVERHEADS] DEPRECIATION EXPENSE: {}%\n".format(depreciation_expense))
        f.write("[CASH DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(day,amt))
        f.write("[CASH DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(day,amt))
        f.write("[PROFIT DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(day,amt))