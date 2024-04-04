
# Needed 
# 1. The total number of months included in the dataset -done *
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period


### start here
import csv

# create variables
# open the file
budget_file_path = "PyBank/Resources/budget_data.csv"
total_months = 0
total_income = 0
previous_income = 0
month_of_change = []
income_change = 0
income_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["",9999999]
income_average = 0
# greatest_decrease = ["", 9999999]
# greatest_increase = ["", 0]
# revenue_change_list = []
# revenue_average = 0

with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file) # skips a row in the file (first row =header row)
     # read a row in the file
    for row in csv_file:
        # add to total months
        total_months+= 1

         #Calculate the total income
        total_income += int(row[1])

    #print(total_income)
        # estimate the average change in incomes between months over the entire period
        income_change = float(row[1]) - previous_income
        previous_income = float(row[1])
        income_change +=  income_change
        month_of_change+= row[0]
        income_change_list = income_change_list + [income_change]
        print(income_change_list)
        


        
        # revenue_change_list = revenue_change_list + [revenue_change]
        # month_of_change = [month_of_change] + [row["Date"]]



        
    #print(income_change)

    # greatest increase in income over the entire period
    if income_change > greatest_increase[1]:
            greatest_increase[1] = income_change[1]
            greatest_increase[0] = row[0]

    #print(greatest_increase)




       # total_amount+=int(row[1])
      #  average = total_amount/total_months

     






# print the results to screen
# print("Financial Analysis")
# print("----------------------------")
# print(f"Total: ${total_amount}")
# print(f"Total Months: {total_months}")
# print(f"Average Change: $-{average}")
# print the results to file



### end here


# example output

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# Determine poverty rate to 2 decimal places, convert to string
        # percent = round(int(row[8]) / int(row[1]) * 100, 2)
        # poverty_rate.append(str(percent) + "%")