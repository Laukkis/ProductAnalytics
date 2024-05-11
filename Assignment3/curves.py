import matplotlib.pyplot as plt
import pandas as pd

# Read data from Excel file
bid_data = pd.read_excel("data.xlsx", sheet_name="bids")

# Filter the data to include only 'IPO bid' rows
ipo_bids= bid_data[bid_data['action'] == 'IPO bid']

ipo_10 = ipo_bids[ipo_bids['shoe_size'] == 10]

# Separate data for red and black shoes
ipo_10_r = ipo_10[ipo_10['product_type'] == 'red']
ipo_10_b = ipo_10[ipo_10['product_type'] == 'black']

# Count bids with the same amount, reverse order and calculate cumulative sum
demand_ipo_10_r = ipo_10_r.groupby('amount')['amount'].count().iloc[::-1].cumsum()
demand_ipo_10_b = ipo_10_b.groupby('amount')['amount'].count().iloc[::-1].cumsum()

# Define price range for supply line based on demand data
min_index = min(demand_ipo_10_r.index.min(), demand_ipo_10_b.index.min())
max_index = max(demand_ipo_10_r.index.max(), demand_ipo_10_b.index.max())

# Creating a constant supply series
supply_10_r = pd.Series(data=[50, 50], index=[min_index, max_index])
supply_10_b = pd.Series(data=[100, 100], index=[min_index, max_index])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(demand_ipo_10_r.index, demand_ipo_10_r.values, 'r-', label='Demand Red')
plt.plot(demand_ipo_10_b.index, demand_ipo_10_b.values, 'k-', label='Demand Black')
plt.plot(supply_10_r.index, supply_10_r.values, 'm--', label='Supply Red')
plt.plot(supply_10_b.index, supply_10_b.values, 'b--', label='Supply Black')

plt.xscale('log')  # Set logarithmic scale for the x-axis
plt.title('Cumulative Demand and Constant Supply for Size 10 Shoes')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()
