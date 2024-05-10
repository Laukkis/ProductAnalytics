import pandas as pd
import matplotlib.pyplot as plt

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

# Calculate IQR for each group of shoe size and color
bid_data['IQR'] = bid_data.groupby(['shoe_size', 'product_type'])['amount'].transform(
    lambda x: x.quantile(0.75) - x.quantile(0.25)
)

# Calculate the upper bound for outliers
bid_data['upper_bound'] = bid_data.groupby(['shoe_size', 'product_type'])['amount'].transform(
    lambda x: x.quantile(0.75) + 1.5 * bid_data['IQR']
)

# Identify the outliers
outliers = bid_data[bid_data['amount'] > bid_data['upper_bound']]

print("Outlier bids:")
print(outliers)
print("Number of outlier rows:", outliers.shape[0])



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