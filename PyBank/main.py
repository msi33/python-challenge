
# Needed 
# 1. The total number of months included in the dataset -done *
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period



# # Importing the necessary modules/libraries
# import csv
# # create variables
# # open the file
# budget_file_path = "Resources/budget_data.csv"




# total_months = 0
# total_income = 0
# dates = []
# profit_loss = []
# total_profit_loss = 0
### start here
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
    next(csv_file) # skips a row in the file (first row = header row)

    # read a row in the file
    for row in csv_file:
        #print(row)
        total_months+= 1 
        total_income += int(row[1])
        date = row[0]
        dates.append(row[0]) # also date above can be used
        print(dates)

        previous_income = int(row[1])
        print(previous_income)
        
        # calculate the change in income
        income_change = total_income - previous_income
        profit_loss.append(income_change)
        
        #print(total_income,previous_income, income_change, profit_loss)
        # Total net amount of profit/losses over entire period
        print(total_profit_loss)


        # Greatest increase in profit
        greatest_increase = max(profit_loss)
        greatest_index = profit_loss.index(greatest_increase)
        greatest_date = dates[greatest_index]
        print(greatest_date)
        

        
















# previous_income = 0
# month_of_change = []
# income_change = 0
# income_change_list = []
# greatest_increase = 0
# greatest_decrease = 0
# income_average = 0



# with open(budget_file_path) as budget_file:
#     csv_file = csv.reader(budget_file)
#     next(csv_file) # skips a row in the file (first row =header row)
#      # read a row in the file
#     for row in csv_file:
#         print(row)
#         # add to total months
#         total_months+= 1
#         #Calculate the total income
#         total_income += int(row[1])
#     print(row)
    
    
    
    
    
    # print(total_income)
    #     previous_income = float(row[1])
    #     income_change =  float(row[1]) - previous_income
    #     profit.append(income_change)
        #print(profit)



      # Calculate the change, then add it to list of changes
        # income_change = int(row[1])-value
        # profits.append(change)
        # value = int(row[1])








    
        # # estimate the average change in incomes between months over the entire period
         #income_change = float(row[1]) - previous_income
        # previous_income = float(row[1])
        # print(previous_income)
        # #Calculate the average change in revenue between months over the entire period
        # revenue_change = float(row["Profit/Losses"])- previous_revenue
        # previous_revenue = float(row["Profit/Losses"])
        # revenue_change_list = revenue_change_list + [revenue_change]
        # month_of_change = [month_of_change] + [row["Date"]]


    #print(previous_income)
        # previous_income = float(row[1])
        # income_change +=  income_change
        # print(income_change)
        # month_of_change+= row[0]
        # income_change_list = income_change_list + [income_change]

    # greatest increase in income over the entire period
    #    greatest_increase = max (income_change)
    
    

# #Greatest increase in profits
#     greatest_increase = max(profits)
#     greatest_index = profits.index(greatest_increase)
#     greatest_date = dates[greatest_index]

#     if income_change > greatest_increase[1]:
#             greatest_increase[1] = income_change[1]
#             greatest_increase[0] = row[0]
#             print(greatest_increase)

#          #The greatest increase in revenue (date and amount) over the entire period
#         if income_change > greatest_increase[1]:
#             greatest_increase[1]= income_change
#             greatest_increase[0] = row['Date']



#  #The greatest increase in revenue (date and amount) over the entire period
#         if revenue_change>greatest_increase[1]:
#             greatest_increase[1]= revenue_change
#             greatest_increase[0] = row['Date']


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

