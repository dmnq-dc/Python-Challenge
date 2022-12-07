#Import Dependencies
import os
import csv

#csv_path = os.path.join('Resources','budget_data.csv') #Relative Path does not work. Tutor has advised to comment this in the code
#csv_path = './Resources/budget_data.csv' #Relative Path does not work. Tutor has advised to comment this in the code

#Open CSV Path
csv_path = os.path.join(r'C:/Users/domin/OneDrive/Documents/Desktop/DV_Bootcamp/Modules\Week 3 - Python/Python-Challenge/PyBank/Resources/budget_data.csv')

#Set initial Variables
month = 0
total_amt = 0
prev_profit= 0
total_profits = 0
date = []
profit_list = []
greatest_inc = ["", 0]
greatest_dec = ["", 99999999999]

#Open csv file, used DictReader to make it easier identifying the columns needed
with open(csv_path, newline= "",) as csv_file:
    csv_reader= csv.DictReader(csv_file)    
    
    #Iterate the following code through each row
    for row in csv_reader:
        
        #Total Months in the file
        month = month + 1

        #Total Amount of Profits
        total_amt = total_amt + int(row["Profit/Losses"])

       #Average Changes in Profits
        ave_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_list = profit_list + [ave_change]
        date = date + [row["Date"]]
        
       #Greatest Increase and Decrease in Profits with Date

        if (ave_change > greatest_inc[1]):
            greatest_inc[1] = ave_change
            greatest_inc[0] = row["Date"]
    
        if (ave_change < greatest_dec[1]):
            greatest_dec[1] = ave_change
            greatest_dec[0] = row["Date"]
            
profit_list.pop(0) #This makes initial cell back to zero
ave_change = sum(profit_list) / len(profit_list)

output = (
        f'\n Financial Analysis\n'
        f'----------------------\n'
        f'Total Months: {month}\n'
        f'Total: ${total_amt}\n'
        f'Average Change: ${ave_change}\n'
        f'Greatest Increase: {greatest_inc[0]} ${greatest_inc[1]}\n'
        f'Greatest Decrease: {greatest_dec[0]} ${greatest_dec[1]}\n'

    )

print(output)

#creating text file and inputing required data
    #Relative Path does not work, tutor has advised to comment the pathway
    #txt_to_output = ".\PyBank\Analysis\pybank_analysis.txt"

txt_to_output = (r"C:\Users\domin\OneDrive\Documents\Desktop\DV_Bootcamp\Modules\Week 3 - Python\Python-Challenge\PyBank\Analysis\pybank_analysis.txt")

with open (txt_to_output, "w") as txt_file:
    output = (
        f'\n Financial Analysis\n'
        f'----------------------\n'
        f'Total Months: {month}\n'
        f'Total: ${total_amt}\n'
        f'Average Change: ${ave_change}\n'
        f'Greatest Increase: {greatest_inc[0]} ${greatest_inc[1]}\n'
        f'Greatest Decrease: {greatest_dec[0]} ${greatest_dec[1]}\n'

    )

#     print(output)
    txt_file.write(output)