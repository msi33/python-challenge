
# Needed 
# 1. The total number of months included in the dataset -done *
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period


### start here
# # Importing the necessary modules/libraries
# import csv
import csv
# create variables
# open the file
budget_file_path = "Resources/budget_data.csv"
total_months = 0
total_income = 0
dates = []
profit_loss = []

with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file) # skips a row in the file (first row = header row)

    # read a row in the file
    for row in csv_file:
        #print(row)
        total_months+= 1 
        total_income += int(row[1])
        date = row[0]
        dates.append(row[0]) # also date above can be used
        #clprint(dates)

        previous_income = int(row[1])
        #print(previous_income)
        
        # calculate the change in income
        income_change = total_income - previous_income
        profit_loss.append(income_change)
        
        #print(total_income,previous_income, income_change, profit_loss)
        # Total net amount of profit/losses over entire period
       # print(profit_loss)


        # Greatest increase in profit
        greatest_increase = max(profit_loss)
        greatest_index = profit_loss.index(greatest_increase)

        greatest_date = dates[greatest_index]
        #print(greatest_increase,greatest_date)

        # Greatest decrease in profit_losses
        greatest_decrease = min(profit_loss)
        loss_index = profit_loss.index(greatest_decrease)
        loss_date = dates[loss_index]
        # print(greatest_decrease,loss_date)
        #Average change in profit/losses between months over entire period
        average_change = sum(profit_loss)/len(profit_loss)
        # print(profit_loss)
        # print(len(profit_loss))
        
# print the results to screen
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_income}")
print(f"Average Change: $-{average_change}")
print(f"Greate Increase in Profits: {greatest_date}$({greatest_increase})")
print(f"Greate Decrease in Profits: {loss_date}$({greatest_decrease})")

# print the results to file

out_file_path = "PyBank\budget_results.txt"
with open(out_file_path,'w') as file_out:
    file_out.write('Financial Analysis\n')
    file_out.write("----------------------------\n")
    file_out.write(f"Total Months: {total_months}\n")
    file_out.write(f"Total: ${total_income}\n")
    file_out.write(f"Average Change: $-{average_change}\n")
    file_out.write(f"Greatest Increase in Profits: {greatest_date}${greatest_increase}\n")
    file_out.write(f"Greatest Decrease in Profits: {loss_date}${greatest_decrease}\n")

# end here

