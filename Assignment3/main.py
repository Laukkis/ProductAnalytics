import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read data from Excel file
bid_data = pd.read_excel("data.xlsx", sheet_name="bids")

# Filter the data to include only 'IPO bid' rows
bid_data = bid_data[bid_data['action'] == 'IPO bid']

# Group bids by shoe size and color, and count the number of bids for each combination
bid_counts = bid_data.groupby(['shoe_size', 'product_type']).size().reset_index(name='num_bids')

print("Count of bids received by shoe size and color:")
print(bid_counts)



##Calculations for correlation between number of bids and quantity available

# Merge the grouped data back to the original data
merged_data = pd.merge(bid_data, bid_counts, on=['shoe_size', 'product_type'])

# Calculate correlation between number of bids and quantity available
bids_quantity_corr = merged_data['num_bids'].corr(merged_data['ipo_supply'])

# Calculate correlation between bid amount and quantity available
bid_amount_quantity_corr = merged_data['amount'].corr(merged_data['ipo_supply'])

print("Correlation between number of bids and quantity available:", bids_quantity_corr)
print("Correlation between bid amount and quantity available:", bid_amount_quantity_corr)

# Interpret the correlations
if abs(bids_quantity_corr) > 0.7:
    print("There is a strong correlation between the number of bids and the quantity available.")
elif abs(bids_quantity_corr) > 0.3:
    print("There is a moderate correlation between the number of bids and the quantity available.")
else:
    print("There is a weak or no correlation between the number of bids and the quantity available.")

if abs(bid_amount_quantity_corr) > 0.7:
    print("There is a strong correlation between the bid amount and the quantity available.")
elif abs(bid_amount_quantity_corr) > 0.3:
    print("There is a moderate correlation between the bid amount and the quantity available.")
else:
    print("There is a weak or no correlation between the bid amount and the quantity available.")


## Calculations for market clearing prices

# Filter the data to include only 'black' and 'red' shoes
black_shoes = bid_data[bid_data['product_type'] == 'black']
red_shoes = bid_data[bid_data['product_type'] == 'red']

# Calculate the median bid amount for each shoe size and color
black_shoes_median_prices = black_shoes.groupby('shoe_size')['amount'].median()
red_shoes_median_prices = red_shoes.groupby('shoe_size')['amount'].median()

print("Market clearing prices for black shoes:")
print(black_shoes_median_prices)

print("Market clearing prices for red shoes:")
print(red_shoes_median_prices)


##Calculations for Outliers with Interquartile Range (IQR) method

filtered_data = bid_data[bid_data['action'] == 'IPO bid'][['shoe_size', 'product_type', 'amount']]


# Creating boxplots for amounts bid on shoes, grouped by shoe size and color
plt.figure(figsize=(12, 6))
boxplot = sns.boxplot(x='shoe_size', y='amount', hue='product_type', data=filtered_data, palette=['red', 'black'])

plt.title('Boxplot of Bids by Shoe Size and Color')
plt.xlabel('Shoe Size')
plt.ylabel('Bid Amount')
plt.yscale('log')  # Using a logarithmic scale to better handle wide variations in amounts
plt.legend(title='Shoe Color')

# Optional: adjusting y-axis to improve visibility of boxes
plt.ylim(1, 10000000)  # Adjust these limits based on the range of your data

plt.show()

def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Filter out the outliers and return them
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Detect outliers for each combination of shoe size and color
outlier_results = {}
for size in filtered_data['shoe_size'].unique():
    for color in filtered_data['product_type'].unique():
        subset = filtered_data[(filtered_data['shoe_size'] == size) & (filtered_data['product_type'] == color)]
        outliers = detect_outliers(subset, 'amount')
        if not outliers.empty:
            outlier_results[(size, color)] = outliers

# Print the results
for key, value in outlier_results.items():
    print(f"Outliers for shoe size {key[0]} and color {key[1]}:\n{value}\n")
## Higher bids

# Calculate average bid amount for each color
avg_bid_by_color = bid_data.groupby('product_type')['amount'].mean()
print("Average bid by color:")
print(avg_bid_by_color)

# Find the color with the highest average bid
highest_avg_bid_color = avg_bid_by_color.idxmax()
print("\nColor with the highest average bid:", highest_avg_bid_color)

# Calculate average bid amount for each shoe size
avg_bid_by_size = bid_data.groupby('shoe_size')['amount'].mean()
print("\nAverage bid by shoe size:")
print(avg_bid_by_size)

# Find the shoe size with the highest average bid
highest_avg_bid_size = avg_bid_by_size.idxmax()
print("\nShoe size with the highest average bid:", highest_avg_bid_size)

# Filter the data to include only realized bids
realized_bids = bid_data[bid_data['match'] == 1]

# Calculate the total revenue from realized bids
total_revenue_realized = realized_bids['amount'].sum()
print("Total revenue from realized bids:", total_revenue_realized)