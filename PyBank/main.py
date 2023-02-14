# Declaring our variables as empty or '0'
csv_data = {}
temp_data = {}
total = 0
temp_total = 0
average_change = 0
greatest_profit = 0
profit_month = ''
greatest_loss = 0
loss_month = ''


# Importing the CSV file 
with open('resources/budget_data.csv', 'r') as file:
    lines = file.read().split('\n')

# Creating a header from Line 1 in the CSV file
header_row = lines[0].split(',')

# Using a for loop to loop through the CSV lines and copy them to a dictionary, in sequential order
for line in range(1, len(lines)):
    data_line = lines[line].split(',')
    temp_data = dict(zip(header_row, data_line))
    csv_data[line] = temp_data


# Printing total months 
print(f'Total Months: ' + str(len(lines) - 1))


# Pulling all dictionary values for Profit/Losses keys, converting strings to integers, add to a running total
for i in range(1, len(lines)):
    temp_total = csv_data[i].get("Profit/Losses")
    temp_total = int(temp_total)
    total += temp_total
print(f'Total: $' + str(total))


# Finding the average change from all the Profit/Losses
average_change = total / 86
# print(f'Average Change: $' + str("%.2f" % average_change))
print(f'Average Change: $' + str(round(average_change, 2)))


# Sorting through the dictionary, checking all Profit/Losses for the greatest positive string, then converting to integer
for i in range(1, len(lines)):
    if int(csv_data[i].get("Profit/Losses")) > greatest_profit:
        greatest_profit = int(csv_data[i].get("Profit/Losses"))
        profit_month = csv_data[i].get("Date")
print(f'Greatest Increase in Profits: ' + profit_month + ' ($' + str(greatest_profit) + ')')


# Finding the average change from all the Profit/Losses
for i in range(1, len(lines)):
    if int(csv_data[i].get("Profit/Losses")) < greatest_loss:
        greatest_loss = int(csv_data[i].get("Profit/Losses"))
        loss_month = csv_data[i].get("Date")
print(f'Greatest Decrease in Profits: ' + loss_month + ' ($' + str(greatest_loss) + ')')


# Export results into a TXT File
f = open('analysis/PyBank_results.txt', 'w')
f.write(f'Total Months: ' + str(len(lines) - 1))
f.write(f'\nTotal: $' + str(total))
f.write(f'\nAverage Change: $' + str(round(average_change, 2)))
f.write(f'\nGreatest Increase in Profits: ' + profit_month + ' ($' + str(greatest_profit) + ')')
f.write(f'\nGreatest Decrease in Profits: ' + loss_month + ' ($' + str(greatest_loss) + ')')
f.close()
