import os
import csv
from pathlib import Path

pybank = os.path.join('PyBank','Resources','budget_data.csv')

months = []
profit = []
profit_change = []
 
with open(pybank,newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget,delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 

        months.append(row[0])
        profit.append(int(row[1]))

    for i in range(len(profit)-1):
        
        profit_change.append(profit[i+1]-profit[i])
        
max_inc = max(profit_change)
max_dec = min(profit_change)

max_inc_month = profit_change.index(max_inc) + 1
max_dec_month = profit_change.index(max_dec) + 1 


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_inc_month]} (${(str(max_inc))})")
print(f"Greatest Decrease in Profits: {months[max_dec_month]} (${(str(max_dec))})")

analysis = Path("PyBank", "analysis","Analysis.txt")

with open(analysis,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_inc_month]} (${(str(max_inc))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_dec_month]} (${(str(max_dec))})")
