
import os
import csv


csvpath = os.path.join('/Users/gallasteguicrino/Desktop/NUCHI201811DATA2/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')


count_months = 0
total_revenue = 0
row_revenue = 0
first_row = True


with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    for row in csvreader:
        count_months = count_months + 1
        total_revenue = total_revenue + float(row[1])
        if(first_row == True):
            first_row = False
            total_change = 0
            max_increase = -1000000
            max_decrease = 1000000
        else:
            total_change = total_change + (float(row[1]) - row_revenue)
            if((float(row[1]) - row_revenue) > max_increase):
                max_increase = float(row[1]) - row_revenue
                max_increase_month = row[0]
            if((float(row[1]) - row_revenue) < max_decrease):
                max_decrease = float(row[1]) - row_revenue
                max_decrease_month = row[0]
  
        row_revenue = float(row[1])

print("____________________________________________________")
print("          Financial Analysis Summary            ")
print("____________________________________________________")
print("Total Months: " + str(count_months))
print("Total: $ " + str(total_revenue))
print("Average Change: $" + str(total_change/(count_months-1)))
print("Greatest Increase in Profits: " + max_increase_month + " ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + max_decrease_month + " ($" + str(max_decrease) + ")")

