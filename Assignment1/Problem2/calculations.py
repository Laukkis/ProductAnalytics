import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl.drawing.image import Image as ExcelImage
import os

excel_file_path = '../dataset.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Switchbacks')

commuting_hours_column = 'commute'
treat = 'treat'

#Make 2 lists, commuting and non commuting hours
commuting_hours = df[df[commuting_hours_column] == True]
non_commuting_hours = df[df[commuting_hours_column] == False]

###COMMUTING HOURS CALCULATIONS

commuting_treat = df[(df['commute'] == True) & (df['treat'] == True)]
commuting_control = df[(df['commute'] == True) & (df['treat'] == False)]

total_trips_treat = commuting_treat['trips_pool'] + commuting_treat['trips_express']
total_trips_control = commuting_control['trips_pool'] + commuting_control['trips_express']

# Calculate the difference in the number of ridesharing trips between treatment and control groups
difference_in_trips = total_trips_treat.sum() - total_trips_control.sum()

print("Difference in the number of ridesharing trips between treatment and control groups during commuting hours:", difference_in_trips)

# Calculate the total number of rider cancellations for each group
total_cancellations_treat = commuting_treat['rider_cancellations']
total_cancellations_control = commuting_control['rider_cancellations']

# Calculate the difference in the number of rider cancellations between treatment and control groups
difference_in_cancellations = total_cancellations_treat.sum() - total_cancellations_control.sum()

print("Difference in the number of rider cancellations between treatment and control groups during commuting hours:", difference_in_cancellations)


# Calculate the total driver payout for each group
total_payout_treat = commuting_treat['total_driver_payout'].sum()
total_payout_control = commuting_control['total_driver_payout'].sum()

# Calculate the total number of ridesharing trips for each group
total_trips_treat = (commuting_treat['trips_pool'] + commuting_treat['trips_express']).sum()
total_trips_control = (commuting_control['trips_pool'] + commuting_control['trips_express']).sum()

# Calculate the average driver payout per trip for each group
avg_payout_per_trip_treat = total_payout_treat / total_trips_treat
avg_payout_per_trip_control = total_payout_control / total_trips_control

# Calculate the difference in average driver payout per trip between treatment and control groups
difference_in_avg_payout_per_trip = avg_payout_per_trip_control-avg_payout_per_trip_treat

print("Difference in average driver payout per trip between treatment and control groups during commuting hours:", difference_in_avg_payout_per_trip)

# Calculate the total number of matches for each group
total_matches_treat = commuting_treat['total_matches'].sum()
total_matches_control = commuting_control['total_matches'].sum()

# Calculate the total number of double matches for each group
total_double_matches_treat = commuting_treat['total_double_matches'].sum()
total_double_matches_control = commuting_control['total_double_matches'].sum()

# Calculate the overall match rate for each group
match_rate_treat = total_double_matches_treat / total_matches_treat if total_matches_treat != 0 else 0
match_rate_control = total_double_matches_control / total_matches_control if total_matches_control != 0 else 0

# Calculate the difference in overall match rate between treatment and control groups
difference_in_match_rate = match_rate_treat - match_rate_control

print("Difference in overall match rate between treatment and control groups during commuting hours:", difference_in_match_rate)



### NON COMMUTING HOURS CALCULATIONS

non_commuting_treat = df[(df['commute'] == False) & (df['treat'] == True)]
non_commuting_control = df[(df['commute'] == False) & (df['treat'] == False)]

# Calculate the total number of ridesharing trips for each group during non-commuting hours
total_trips_non_commuting_treat = (non_commuting_treat['trips_pool'] + non_commuting_treat['trips_express']).sum()
total_trips_non_commuting_control = (non_commuting_control['trips_pool'] + non_commuting_control['trips_express']).sum()

# Calculate the difference in the number of ridesharing trips between treatment and control groups during non-commuting hours
difference_in_trips_non_commuting = total_trips_non_commuting_treat - total_trips_non_commuting_control

print("Difference in the number of ridesharing trips between treatment and control groups during non-commuting hours:", difference_in_trips_non_commuting)

# Calculate the total number of rider cancellations for each group during non-commuting hours
total_cancellations_non_commuting_treat = non_commuting_treat['rider_cancellations'].sum()
total_cancellations_non_commuting_control = non_commuting_control['rider_cancellations'].sum()

# Calculate the difference in the number of rider cancellations between treatment and control groups during non-commuting hours
difference_in_cancellations_non_commuting = total_cancellations_non_commuting_treat - total_cancellations_non_commuting_control

print("Difference in the number of rider cancellations between treatment and control groups during non-commuting hours:", difference_in_cancellations_non_commuting)


# Calculate the total driver payout for each group during non-commuting hours
total_payout_non_commuting_treat = non_commuting_treat['total_driver_payout'].sum()
total_payout_non_commuting_control = non_commuting_control['total_driver_payout'].sum()

# Calculate the total number of ridesharing trips for each group during non-commuting hours
total_trips_non_commuting_treat = (non_commuting_treat['trips_pool'] + non_commuting_treat['trips_express']).sum()
total_trips_non_commuting_control = (non_commuting_control['trips_pool'] + non_commuting_control['trips_express']).sum()

#-------- Q9---------------

treatment_commuting_double_matches = df[(df['commute'] == True) & (df['treat'] == True)]['total_double_matches'].sum()
treatment_commuting_matches = df[(df['commute'] == True) & (df['treat'] == True)]['total_matches'].sum()
treatment_commuting_double_match_rate = treatment_commuting_double_matches / treatment_commuting_matches

# Calculate double match rate for control group during commuting hours
control_commuting_double_matches = df[(df['commute'] == True) & (df['treat'] == False)]['total_double_matches'].sum()
control_commuting_matches = df[(df['commute'] == True) & (df['treat'] == False)]['total_matches'].sum()
control_commuting_double_match_rate = control_commuting_double_matches / control_commuting_matches

# Calculate the difference in double match rate between treatment and control groups during commuting hours
double_match_rate_difference = treatment_commuting_double_match_rate - control_commuting_double_match_rate

# Print the difference in double match rate
print("Q9: Difference in double match rate between treatment and control groups during commuting hours:", double_match_rate_difference)

# Calculate the average driver payout per trip for each group during non-commuting hours
avg_payout_per_trip_non_commuting_treat = total_payout_non_commuting_treat / total_trips_non_commuting_treat if total_trips_non_commuting_treat != 0 else 0
avg_payout_per_trip_non_commuting_control = total_payout_non_commuting_control / total_trips_non_commuting_control if total_trips_non_commuting_control != 0 else 0

# Calculate the difference in average driver payout per trip between treatment and control groups during non-commuting hours
difference_in_avg_payout_per_trip_non_commuting = avg_payout_per_trip_non_commuting_treat - avg_payout_per_trip_non_commuting_control

print("Difference in average driver payout per trip between treatment and control groups during non-commuting hours:", difference_in_avg_payout_per_trip_non_commuting)


# Calculate the total number of matches for each group during non-commuting hours
total_matches_non_commuting_treat = non_commuting_treat['total_matches'].sum()
total_matches_non_commuting_control = non_commuting_control['total_matches'].sum()

# Calculate the total number of double matches for each group during non-commuting hours
total_double_matches_non_commuting_treat = non_commuting_treat['total_double_matches'].sum()
total_double_matches_non_commuting_control = non_commuting_control['total_double_matches'].sum()

# Calculate the overall match rate for each group during non-commuting hours
match_rate_non_commuting_treat = total_double_matches_non_commuting_treat / total_matches_non_commuting_treat if total_matches_non_commuting_treat != 0 else 0
match_rate_non_commuting_control = total_double_matches_non_commuting_control / total_matches_non_commuting_control if total_matches_non_commuting_control != 0 else 0

# Calculate the difference in overall match rate between treatment and control groups during non-commuting hours
difference_in_match_rate_non_commuting = match_rate_non_commuting_treat - match_rate_non_commuting_control

print("Difference in overall match rate between treatment and control groups during non-commuting hours:", difference_in_match_rate_non_commuting)

#Q20. What is the difference in double match rate between the treatment and control groups during

# Filter data for treatment and control groups during non-commuting hours
treatment_non_commuting_double_matches = df[(df['commute'] == False) & (df['treat'] == True)]['total_double_matches']
control_non_commuting_double_matches = df[(df['commute'] == False) & (df['treat'] == False)]['total_double_matches']

# Calculate the total number of matches for each group during non-commuting hours
treatment_non_commuting_matches = df[(df['commute'] == False) & (df['treat'] == True)]['total_matches'].sum()
control_non_commuting_matches = df[(df['commute'] == False) & (df['treat'] == False)]['total_matches'].sum()

# Calculate the double match rate for each group during non-commuting hours
treatment_non_commuting_double_match_rate = treatment_non_commuting_double_matches.sum() / treatment_non_commuting_matches
control_non_commuting_double_match_rate = control_non_commuting_double_matches.sum() / control_non_commuting_matches

# Calculate the difference in double match rate between treatment and control groups during non-commuting hours
double_match_rate_difference_non_commuting = treatment_non_commuting_double_match_rate - control_non_commuting_double_match_rate

# Print the difference in double match rate during non-commuting hours
print("Q20: Difference in double match rate between treatment and control groups during non-commuting hours:", double_match_rate_difference_non_commuting)
