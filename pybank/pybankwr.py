# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:33:55 2019

@author: gargi
"""
import os
import csv

budget_data = os.path.join("budget_data.csv")

total_months = 0
total_revenue = 0
revenue = 0
revenue_change = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")
   csv_header = next(csvreader)
   first_row = next(csvreader)  
   total_months += 1
   total_revenue += int(first_row[1])
   revenue = int(first_row[1])
   
   for row in csvreader:
       dates.append(row[0])
       revenue_change = int(row[1])-revenue
       profits.append(revenue_change)
       revenue = int(row[1])
       total_months += 1
       total_revenue = total_revenue +int(row[1])
       
   Greatest_increase = max(profits)
   Greatest_index = profits.index(Greatest_increase)
   Greatest_date = dates[Greatest_index]
   Greatest_decrease = min(profits)
   loss_index = profits.index(Greatest_decrease)
   loss_date = dates[loss_index]
   avg_change = sum(profits)/len(profits)
   
   
print("Financial Analysis")
print("----------------------")
print(f"Total months: {str(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})")
print(f"Greatest Decrease in Profits: {loss_date} (${str(Greatest_decrease)})")

with open('budget_data.txt', 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------' + '\n')
    text.write(f"Total months: {str(total_months)}" + '\n')
    text.write(f"Total: ${str(total_revenue)}" + '\n')
    text.write(f"Average Change: ${str(round(avg_change,2))}" + '\n')
    text.write(f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})" + '\n')
    text.write(f"Greatest Decrease in Profits: {loss_date} (${str(Greatest_decrease)})" + ')'+ '\n')
    
    
    





