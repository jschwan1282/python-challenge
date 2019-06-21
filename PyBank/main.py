import os
import csv

# Set path for file
csvpath = os.path.join("..", "PyBank", "budget-data.csv")

#Create lists for money and months
money=[]
months=[]
# to keep track of change from month to month
monthly_changes=[]
# to keep track of month of change
monthly_changes_month=[]

#read csv and parse data into lists
#money will be a list of integers
with open(csvpath, 'r') as csvfile:
   csvread = csv.reader(csvfile)

   next(csvread, None)

   for row in csvread:
       months.append(row[0])
       money.append(int(row[1]))

 
#find total months
total_months = len(months)

for i in range(len(money)-1):
   # collect change from month to month in money
   monthly_changes.append(money[i+1]-money[i])
   monthly_changes_month.append(months[i])

#calculate average_change
average_change = (sum(monthly_changes)/len(monthly_changes))
#make it a decimal!
average_again = round(average_change, 2)

#create greatest increase and decrease variables and set them equal to the first money entry
#set total revenue = 0
greatest_inc = money[0]
greatest_dec = money[0]
total_money = 0

#loop through money and compare # to find greatest inc and dec
#also add each money to total 
for r in range(len(monthly_changes)):
   if monthly_changes[r] >= greatest_inc:
       greatest_inc = monthly_changes[r]
       great_inc_month = months[r]
   elif monthly_changes[r] <= greatest_dec:
       greatest_dec = monthly_changes[r]
       great_dec_month = months[r]
   total_money += monthly_changes[r]    


#sets path for output file
output_dest = os.path.join("..", "PyBank", "budegetsummary.txt")

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
   writefile.writelines('Financial Analysis\n')
   writefile.writelines('----------------------------' + '\n')
   writefile.writelines('Total Months: ' + str(total_months) + '\n')
   writefile.writelines('Total Revenue: $' + str(total_money) + '\n')
   writefile.writelines('Average Revenue Change: $' + str(average_again) + '\n')
   writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
   writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
   print(readfile.read())