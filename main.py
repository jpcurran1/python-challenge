import os
import pandas as pd


# data input
budget_df = pd.read_csv('budget_data.csv')

print("Fiancial Analysis")
print("-------------------------")

# count of months
unique_months = len(budget_df['Date'].value_counts())
print('Total Months: ' + str(unique_months))

# total $
total_amount = budget_df['Profit/Losses'].sum()
print('Total: $' + str(total_amount))

# average change
budget_df['change'] = budget_df['Profit/Losses'].diff()
average_change = round(budget_df['change'].mean(), 2)
print('Average Change: $' + str(average_change))

# greatest increase
max_increase = round(budget_df['change'].max(), 0)
max_increase_date = budget_df.loc[budget_df['change'].idxmax(), 'Date']
max_decrease = round(budget_df['change'].min(), 0)
max_decrease_date = budget_df.loc[budget_df['change'].idxmin(), 'Date']


print("Greatest Increase in Profits: " + max_increase_date + " ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + max_decrease_date + " ($" + str(max_decrease) + ")")

    



