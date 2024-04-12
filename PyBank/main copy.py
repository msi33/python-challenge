#Importing the necessary modules/libraries
import csv

# create variables
# open the file
budget_file_path = "Resources/budget_data.csv"

total_months = 0
total_income = 0
dates = []
profit_loss = []
total_profit_loss = 0

with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file) # skips a row in the file (first row =header row)
     
     
     # read a row in the file
    for row in csv_file: 
        #print(row)
        total_months +=1
        total_income += int(row[1])
        date = row[0]
        dates.append(row[0])
        previous_income =int(row[1])
    
        # calculate the change 
        income_change = total_income - previous_income
    
        profit_loss.append(income_change)
        #print(total_income,previous_income, income_change,profit_loss)

        # Total net amount of profit/losses over entire period
        total_profit_loss +=int(row[1])
        print(total_profit_loss)

        # Greatest increase in profit
        greatest_increase = max(profit_loss)
        greatest_index =profit_loss.index(greatest_increase)
        greatest_date = dates[greatest_index] 

        #print(greatest_increase,greatest_date)

        # Greatest decrease in profit_losses
        greatest_decrease = min(profit_loss)
        loss_index = profit_loss.index(greatest_decrease)
        loss_date =dates[loss_index]


    #average change in profit/losses between months over entire period
    avg_change = sum(profit_loss)/len(profit_loss)
#print(avg_change)
print(profit_loss)
# print the results to screen
print("Financial Analysis")
print("----------------------------")
print(f"Total: ${total_income}")
print(f"Total Months: {total_months}")
print(f"Average Change: $-{avg_change}")
print(f"Greatest Increase in Profits: {date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date} (${greatest_decrease})")