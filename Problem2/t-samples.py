import pandas as pd

from scipy import stats

excel_file_path = '../dataset.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Switchbacks')

alpha = 0.05  # significance level


##---------------PROBLEM 2 COMMUTING--------------------------

#Q: 1. What is the difference in the number of ridesharing trips between the treatment and control

commuting_treat = df[(df['commute'] == True) & (df['treat'] == True)]
commuting_control = df[(df['commute'] == True) & (df['treat'] == False)]

trips_treat = (commuting_treat['trips_pool'] + commuting_treat['trips_express']).values
trips_control = (commuting_control['trips_pool'] + commuting_control['trips_express']).values

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(trips_treat, trips_control)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results
if p_value < alpha:
    print("Q2: Reject the null hypothesis: There is a significant difference in the number of ridesharing trips.")
else:
    print("Q2: Fail to reject the null hypothesis: There is no significant difference in the number of ridesharing trips.")


#Q: 3. What is the difference in the number of rider cancellations between the treatment and control

cancellations_treat = commuting_treat['rider_cancellations'].values
cancellations_control = commuting_control['rider_cancellations'].values

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(cancellations_treat, cancellations_control)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Q4: Reject the null hypothesis: There is a significant difference in the number of rider cancellations.")
else:
    print("Q4: Fail to reject the null hypothesis: There is no significant difference in the number of rider cancellations.")


#Q 7. What is the difference in overall match rate between the treatment and control groups during
    

 # Calculate the overall match rate for each group during commuting hours
match_rate_treat = (commuting_treat['total_double_matches'] / commuting_treat['total_matches']).values
match_rate_control = (commuting_control['total_double_matches'] / commuting_control['total_matches']).values

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(match_rate_treat, match_rate_control)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Q8: Reject the null hypothesis: There is a significant difference in the overall match rate.")
else:
    print("Q8: Fail to reject the null hypothesis: There is no significant difference in the overall match rate.")   


##---------------PROBLEM 2 NON-COMMUTING--------------------------

#Q12. What is the difference in the number of ridesharing trips between the treatment and control

non_commuting_treat = df[(df['commute'] == False) & (df['treat'] == True)]
non_commuting_control = df[(df['commute'] == False) & (df['treat'] == False)]

# Extract the number of ridesharing trips for each group during non-commuting hours
trips_treat = (non_commuting_treat['trips_pool'] + non_commuting_treat['trips_express']).values
trips_control = (non_commuting_control['trips_pool'] + non_commuting_control['trips_express']).values

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(trips_treat, trips_control)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Q13: Reject the null hypothesis: There is a significant difference in the number of ridesharing trips.")
else:
    print("Q13: Fail to reject the null hypothesis: There is no significant difference in the number of ridesharing trips.")


#Q14. What is the difference in the number of rider cancellations between the treatment and control

cancellations_treat = non_commuting_treat['rider_cancellations'].values
cancellations_control = non_commuting_control['rider_cancellations'].values

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(cancellations_treat, cancellations_control)

# Print the results
print("Q15")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the number of rider cancellations.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the number of rider cancellations.")


#Q16. What is the difference in driver payout per trip between the treatment and control groups
    

total_payout_non_commuting_treat = (non_commuting_treat['total_driver_payout']).values
total_payout_non_commuting_control = (non_commuting_control['total_driver_payout']).values

# Calculate the total number of ridesharing trips for each group during non-commuting hours
total_trips_non_commuting_treat = (non_commuting_treat['trips_pool'] + non_commuting_treat['trips_express']).values
total_trips_non_commuting_control = (non_commuting_control['trips_pool'] + non_commuting_control['trips_express']).values

# Calculate the average driver payout per trip for each group during non-commuting hours
avg_payout_per_trip_non_commuting_treat = total_payout_non_commuting_treat / total_trips_non_commuting_treat
avg_payout_per_trip_non_commuting_control = total_payout_non_commuting_control / total_trips_non_commuting_control

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(avg_payout_per_trip_non_commuting_treat, avg_payout_per_trip_non_commuting_control)

# Print the results
print("Q17")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the driver payout per trip.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the driver payout per trip.")   

#Q18. What is the difference in overall match rate between the treatment and control groups during
    
match_rate_non_commuting_treat = (non_commuting_treat['total_double_matches'] / non_commuting_treat['total_matches']).values
match_rate_non_commuting_control = (non_commuting_control['total_double_matches'] / non_commuting_control['total_matches']).values

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(match_rate_non_commuting_treat, match_rate_non_commuting_control)

# Print the results
print("Q19")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret the results

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the overall match rate.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the overall match rate.")


#Q9. What is the difference in double match rate between the treatment and control groups during
    
treatment_commuting_double_matches = df[(df['commute'] == True) & (df['treat'] == True)]['total_double_matches']
control_commuting_double_matches = df[(df['commute'] == True) & (df['treat'] == False)]['total_double_matches']

# Perform t-test
t_statistic, p_value = stats.ttest_ind(treatment_commuting_double_matches, control_commuting_double_matches, equal_var=False)

# Print the t-statistic and p-value
print("Q10")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Check if the result is statistically significant

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in double match rate between treatment and control groups during commuting hours.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in double match rate between treatment and control groups during commuting hours.")


#Q21 

treatment_non_commuting_double_matches = df[(df['commute'] == False) & (df['treat'] == True)]['total_double_matches']
control_non_commuting_double_matches = df[(df['commute'] == False) & (df['treat'] == False)]['total_double_matches']

# Perform t-test
t_statistic_non_commuting, p_value_non_commuting = stats.ttest_ind(treatment_non_commuting_double_matches, control_non_commuting_double_matches, equal_var=False)

# Print the t-statistic and p-value
print('Q21')
print("t-statistic:", t_statistic_non_commuting)
print("p-value:", p_value_non_commuting)

# Check if the result is statistically significant

if p_value_non_commuting < alpha:
    print("Reject the null hypothesis: There is a significant difference in double match rate between treatment and control groups during non-commuting hours.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in double match rate between treatment and control groups during non-commuting hours.")