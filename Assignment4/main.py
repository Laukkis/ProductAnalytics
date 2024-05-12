import numpy as np
import pandas as pd

july_data = pd.read_excel("data.xlsx", sheet_name="July data")

# Filter the data for customers who received promotions and those who did not
promotion_group = july_data[july_data['promotion'] == 1]['renew']
no_promotion_group = july_data[july_data['promotion'] == 0]['renew']

# Calculate the renewal rates for both groups
renewal_rate_promotion = np.mean(promotion_group)
renewal_rate_no_promotion = np.mean(no_promotion_group)

# Print renewal rates for comparison
print("Renewal Rate with Promotion: {:.2%}".format(renewal_rate_promotion))
print("Renewal Rate without Promotion: {:.2%}".format(renewal_rate_no_promotion))

# Calculate the average CLV for both groups
average_clv_promoted = july_data[july_data['promotion'] == 1]['clv'].mean()
average_clv_non_promoted = july_data[july_data['promotion'] == 0]['clv'].mean()

# Print average CLVs for comparison
print("Average CLV for Promoted Customers: ${:.2f}".format(average_clv_promoted))
print("Average CLV for Non-Promoted Customers: ${:.2f}".format(average_clv_non_promoted))
