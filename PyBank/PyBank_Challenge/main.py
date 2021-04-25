
# import modules 
import os 
import csv
# setting path 


csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # print(csvreader)
    csv_header = next(csvreader) # since file has header 
    # print(f"CSV Header:{csv_header}")
    
    count_months = 0 # set counter 
    total_profit = 0 # initializer to get su from profit /loss 
    total_profit_l = [] # initialize new list 
    total_months_l = [] # to create sube list by appending 
    profit_change = [] # to create sube list by appending 
    for row in csvreader: # loop though line
        #print(row)
        count_months = count_months + 1  # counted months by incrementing 
        total_profit = total_profit + round(int(row[1]), 0) # toatl profit  by incremeneting 
        
        total_months_l.append(row[0])  # creating new list buy appending for months 
        total_profit_l.append(int(row[1])) # creating new list by appending to find monthly profit change

    for i in range(len(total_profit_l)-1):# lope through new_list 
        profit_change.append(total_profit_l[i+1] - total_profit_l[i]) # accessing next and prev value by array index 

max_increase = max(profit_change)  # using max function from python & storing it
min_decrease = min(profit_change) # using min ___||____

max_increase_month = profit_change.index(max(profit_change))+1 # fixed error of out of range
min_decrease_month = profit_change.index(max(profit_change))+1 # the same thing
# formatting  everything to match with the outcome.
print()
print("Financial Analysis ")
print("-------------------------")
print(f"Total months: {count_months}")
print(f"Total: ${total_profit}") 
print(f"Average change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months_l[max_increase_month]} (${max_increase})") 
print(f"Greatest Decrease in Profits: {total_months_l[min_decrease_month]} (${min_decrease})") 

# output file/write as .txt 

output_file = os.path.join('financial_analysis.txt')

with open(output_file,"w") as datafile:

    datafile.write("Financial Analysis ")
    datafile.write("\n")
    datafile.write("-------------------------")
    datafile.write("\n")
    datafile.write(f"Total months: {count_months}")
    datafile.write("\n")
    datafile.write(f"Total: ${total_profit}")
    datafile.write("\n") 
    datafile.write(f"Average change: {round(sum(profit_change)/len(profit_change),2)}")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Profits: {total_months_l[max_increase_month]} (${max_increase})")
    datafile.write("\n")
    datafile.write(f"Greatest Decrease in Profits: {total_months_l[min_decrease_month]} (${min_decrease})")
    datafile.write("\n")
    