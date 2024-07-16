import pandas as pd
from pathlib import Path
# Load the data
file_path = "PyBank/Resources/budget_data.csv"
data = pd.read_csv(file_path)
# Calculate the total number of months
total_months = data['Date'].nunique()

# Calculate the net total amount of "Profit/Losses"
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses"
data['Change'] = data['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = data['Change'].mean()

# Find the greatest increase in profits (date and amount)
greatest_increase = data.loc[data['Change'].idxmax()]

# Find the greatest decrease in profits (date and amount)
greatest_decrease = data.loc[data['Change'].idxmin()]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})")

# Export the results to a text file
output_file_path = 'PyBank/Analysis/financial_analysis.txt'
with open(output_file_path, 'w') as file:

    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})\n")
