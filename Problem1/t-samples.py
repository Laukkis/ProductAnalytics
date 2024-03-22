import pandas as pd

from scipy import stats

excel_file_path = '../dataset.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Switchbacks')

alpha = 0.05  # significance level


#Q2 What is the difference in the number of ridesharing trips between commuting and non-commuting hours?

commuting_hours = df[df['commute'] == True]
non_commuting_hours = df[df['commute'] == False]

# Calculate the total number of ridesharing trips for commuting and non-commuting hours
commuting_trips = commuting_hours['trips_pool'] + commuting_hours['trips_express']
non_commuting_trips = non_commuting_hours['trips_pool'] + non_commuting_hours['trips_express']

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind(commuting_trips, non_commuting_trips)

# Print the results
print("Q3:")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the number of ridesharing trips between commuting and non-commuting hours.")
    print("Commuting hours experience a higher number of ridesharing trips compared to non-commuting hours.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the number of ridesharing trips between commuting and non-commuting hours.")

#Q2 What is the difference in the number of ridesharing trips between commuting and non-commuting hours?
    
commuting_express_share = commuting_hours['trips_express'] / (commuting_hours['trips_pool'] + commuting_hours['trips_express'])
non_commuting_express_share = non_commuting_hours['trips_express'] / (non_commuting_hours['trips_pool'] + non_commuting_hours['trips_express'])

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind(commuting_express_share, non_commuting_express_share)

# Print the results
print("Q6:")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the share of Express trips between commuting and non-commuting hours.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the share of Express trips between commuting and non-commuting hours.")

#Q7 Assume that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride. What is the difference in revenues between commuting and non-commuting hours?
    

commuting_pool_revenue = commuting_hours['trips_pool'].fillna(0).sum() * 12.5
non_commuting_pool_revenue = non_commuting_hours['trips_pool'].fillna(0).sum() * 12.5


commuting_express_revenue = commuting_hours['trips_express'].fillna(0).sum() * 10
non_commuting_express_revenue = non_commuting_hours['trips_express'].fillna(0).sum() * 10

# Calculate total revenue for each period
total_commuting_revenue = commuting_pool_revenue + commuting_express_revenue
total_non_commuting_revenue = non_commuting_pool_revenue + non_commuting_express_revenue

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind([total_commuting_revenue], [total_non_commuting_revenue])

# Print the results
print("Q8:")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in revenues between commuting and non-commuting hours.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in revenues between commuting and non-commuting hours.")


#Q9
    
# Define average revenue per ride
average_revenue_pool = 12.5
average_revenue_express = 10

# Calculate revenue from POOL and Express rides during commuting and non-commuting hours
commuting_pool_revenue = commuting_hours['trips_pool'].sum() * average_revenue_pool
non_commuting_pool_revenue = non_commuting_hours['trips_pool'].sum() * average_revenue_pool

commuting_express_revenue = commuting_hours['trips_express'].sum() * average_revenue_express
non_commuting_express_revenue = non_commuting_hours['trips_express'].sum() * average_revenue_express

# Calculate total revenue for each period
total_commuting_revenue = commuting_pool_revenue + commuting_express_revenue
total_non_commuting_revenue = non_commuting_pool_revenue + non_commuting_express_revenue

# Calculate total number of trips for each period
total_commuting_trips = (commuting_hours['trips_pool'].sum() +
                         commuting_hours['trips_express'].sum())
total_non_commuting_trips = (non_commuting_hours['trips_pool'].sum() +
                             non_commuting_hours['trips_express'].sum())

# Calculate profit per trip for each period
profit_per_trip_commuting = total_commuting_revenue / total_commuting_trips
profit_per_trip_non_commuting = total_non_commuting_revenue / total_non_commuting_trips

# Perform t-test
t_statistic, p_value = stats.ttest_ind([profit_per_trip_commuting], [profit_per_trip_non_commuting])


print('Q10:')
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in profits per trip between commuting and non-commuting hours.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in profits per trip between commuting and non-commuting hours.")