import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl.drawing.image import Image as ExcelImage
import os

excel_file_path = '../dataset.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Switchbacks')

commuting_hours_column = 'commute'

#Make 2 lists, commuting and non commuting hours
commuting_hours = df[df[commuting_hours_column] == True]
non_commuting_hours = df[df[commuting_hours_column] == False]

#Lets calculate total ridesharings for each list
commuting_rideshare_trips = commuting_hours['trips_pool'] + commuting_hours['trips_express']
non_commuting_rideshare_trips = non_commuting_hours['trips_pool'] + non_commuting_hours['trips_express']

print("Total ridesharing trips during commuting hours:", commuting_rideshare_trips.sum())
print("Total ridesharing trips during non-commuting hours:", non_commuting_rideshare_trips.sum())

# Calculate the difference in ridesharing trips between commuting and non-commuting hours
rides_diff = commuting_rideshare_trips.sum() - non_commuting_rideshare_trips.sum()
print("Difference in ridesharing trips between commuting and non-commuting hours:", rides_diff)

# Calculate the number of Express rides during commuting and non-commuting hours
express_commuting_rides = commuting_hours['trips_express'].sum()
express_non_commuting_rides = non_commuting_hours['trips_express'].sum()
print("Express commuting rides:", express_commuting_rides)
print("Express non-commuting rides:", express_non_commuting_rides)

# Calculate the difference in express trips between commuting and non-commuting hours
express_diff = express_commuting_rides.sum() - express_non_commuting_rides.sum()
print("Difference in ridesharing trips between commuting and non-commuting hours:", express_diff)

# Calculate the proportion of Express rides to total rides during commuting and non-commuting hours
express_commuting_rate = express_commuting_rides/commuting_rideshare_trips
express_non_commuting_rate = express_non_commuting_rides/non_commuting_rideshare_trips

# Calculate the average rate of Express rides during commuting and non-commuting hours
commuting_express_rate = commuting_hours['trips_express'].mean()
non_commuting_express_rate = non_commuting_hours['trips_express'].mean()

# Print the results
print("Average Express rides during commuting hours:", commuting_express_rate)
print("Average Express rides during non-commuting hours:", non_commuting_express_rate)

# Compare the rates
if commuting_express_rate > non_commuting_express_rate:
    print("Riders use Express at higher rates during commuting hours compared to non-commuting hours.")
else:
    print("Riders do not use Express at higher rates during commuting hours compared to non-commuting hours.")

# Calculate revenue from POOL rides during commuting and non-commuting hours
commuting_pool_revenue = commuting_hours['trips_pool'].sum() * 12.5
non_commuting_pool_revenue = non_commuting_hours['trips_pool'].sum() * 12.5

# Calculate revenue from Express rides during commuting and non-commuting hours
commuting_express_revenue = commuting_hours['trips_express'].sum() * 10
non_commuting_express_revenue = non_commuting_hours['trips_express'].sum() * 10

# Calculate total revenue for each period
total_commuting_revenue = commuting_pool_revenue + commuting_express_revenue
total_non_commuting_revenue = non_commuting_pool_revenue + non_commuting_express_revenue

# Calculate the difference in revenues
revenue_difference = total_commuting_revenue - total_non_commuting_revenue

# Print the difference in revenues
print("Difference in revenues between commuting and non-commuting hours: $", revenue_difference)


#-------- Q9---------------

# Calculate revenue from POOL rides during commuting and non-commuting hours
commuting_pool_revenue = commuting_hours['trips_pool'].sum() * 12.5
non_commuting_pool_revenue = non_commuting_hours['trips_pool'].sum() * 12.5

# Calculate revenue from Express rides during commuting and non-commuting hours
commuting_express_revenue = commuting_hours['trips_express'].sum() * 10
non_commuting_express_revenue = non_commuting_hours['trips_express'].sum() * 10

# Calculate total revenue for each period
total_commuting_revenue = commuting_pool_revenue + commuting_express_revenue
total_non_commuting_revenue = non_commuting_pool_revenue + non_commuting_express_revenue

# Calculate the total number of trips during commuting and non-commuting hours
total_commuting_trips = commuting_hours['trips_pool'].sum() + commuting_hours['trips_express'].sum()
total_non_commuting_trips = non_commuting_hours['trips_pool'].sum() + non_commuting_hours['trips_express'].sum()

# Calculate the profit per trip during commuting and non-commuting hours
profit_per_trip_commuting = total_commuting_revenue / total_commuting_trips
profit_per_trip_non_commuting = total_non_commuting_revenue / total_non_commuting_trips

# Calculate the difference in profits per trip
profit_per_trip_difference = profit_per_trip_commuting - profit_per_trip_non_commuting

# Print the difference in profits per trip in dollars
print("Difference in profits per trip between commuting and non-commuting hours: $", round(profit_per_trip_difference, 2))









result_df = pd.DataFrame({
    'Time Period': ['Commuting Hours', 'Non-Commuting Hours'],
    'Total Ridesharing Trips': [commuting_rideshare_trips.sum(), non_commuting_rideshare_trips.sum(),],
    'Total Ridesharing difference': ['', rides_diff],
    'Express Rides': [express_commuting_rides, express_non_commuting_rides],
    'Express rides difference': ['', express_diff],
    
})


#Lets then make chart
fig, ax = plt.subplots()

ax.bar("Commuting Hours", commuting_rideshare_trips.sum(), label='Ridesharing Trips')
ax.bar("Non-Commuting Hours", non_commuting_rideshare_trips.sum(), label='Ridesharing Trips')

ax.set_ylabel('Total Ridesharing Trips')
ax.set_title('Ridesharing Trips Comparison between Commuting and Non-Commuting Hours')
ax.legend()


# Save the results
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
result_folder_path = f'./results_{timestamp}'
os.makedirs(result_folder_path, exist_ok=True)

result_excel_path = f'{result_folder_path}/result_chart_v{timestamp}.xlsx'
chart_image_path = f'{result_folder_path}/chart_v{timestamp}.png'

result_df.to_excel(result_excel_path, index=False)

plt.savefig(chart_image_path)
plt.close()

with pd.ExcelWriter(result_excel_path, engine='openpyxl', mode='a') as writer:
    chart_image = ExcelImage(chart_image_path)
    chart_worksheet = writer.sheets['Sheet1'] 
    chart_worksheet.add_image(chart_image, 'D4')

print(f"Results and chart saved to {result_excel_path}")