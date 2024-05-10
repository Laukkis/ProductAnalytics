import matplotlib.pyplot as plt
import pandas as pd

# Read data from Excel file
bid_data = pd.read_excel("data.xlsx", sheet_name="bids")

# Filter the data to include only 'IPO bid' rows
bid_data = bid_data[bid_data['action'] == 'IPO bid']

bid_counts = bid_data.groupby(['shoe_size', 'product_type']).size().reset_index(name='num_bids')

# Filter the data to include only 'black' and 'red' shoes
black_shoes = bid_data[bid_data['product_type'] == 'black']
red_shoes = bid_data[bid_data['product_type'] == 'red']

# Filter the data to include only size 10 shoes
size_10_black_shoes = black_shoes[black_shoes['shoe_size'] == 10]
size_10_red_shoes = red_shoes[red_shoes['shoe_size'] == 10]

# Merge size_10_black_shoes with bid_counts
size_10_black_shoes = pd.merge(size_10_black_shoes, bid_counts, on=['shoe_size', 'product_type'])

# Merge size_10_red_shoes with bid_counts
size_10_red_shoes = pd.merge(size_10_red_shoes, bid_counts, on=['shoe_size', 'product_type'])

# Group by bid amount and calculate the sum of bids and IPO supply
black_shoes_grouped = size_10_black_shoes.groupby('amount').agg({'num_bids': 'sum', 'ipo_supply': 'sum'})
red_shoes_grouped = size_10_red_shoes.groupby('amount').agg({'num_bids': 'sum', 'ipo_supply': 'sum'})

# Plot demand and supply curves for black shoes
plt.figure(figsize=(10, 5))
plt.plot(black_shoes_grouped.index, black_shoes_grouped['num_bids'], label='Demand')
plt.plot(black_shoes_grouped.index, black_shoes_grouped['ipo_supply'], label='Supply')
plt.title('Demand and Supply Curves for Size 10 Black Shoes')
plt.xlabel('Bid Amount')
plt.ylabel('Number of Bids / IPO Supply')
plt.legend()
plt.show()

# Plot demand and supply curves for red shoes
plt.figure(figsize=(10, 5))
plt.plot(red_shoes_grouped.index, red_shoes_grouped['num_bids'], label='Demand')
plt.plot(red_shoes_grouped.index, red_shoes_grouped['ipo_supply'], label='Supply')
plt.title('Demand and Supply Curves for Size 10 Red Shoes')
plt.xlabel('Bid Amount')
plt.ylabel('Number of Bids / IPO Supply')
plt.legend()
plt.show()