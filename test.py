import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl.drawing.image import Image as ExcelImage
import os



excel_file_path = './dataset.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Switchbacks')


print(df.columns)

commuting_hours_column = 'commute'

#Make 2 lists, commuting and non commuting hours
commuting_hours = df[df[commuting_hours_column] == True]
non_commuting_hours = df[df[commuting_hours_column] == False]


#Lets calculate total ridesharings for each list
commuting_rideshare_trips = commuting_hours['trips_pool'] + commuting_hours['trips_express']
non_commuting_rideshare_trips = non_commuting_hours['trips_pool'] + non_commuting_hours['trips_express']

print("Total ridesharing trips during commuting hours:", commuting_rideshare_trips.sum())
print("Total ridesharing trips during non-commuting hours:", non_commuting_rideshare_trips.sum())

result_df = pd.DataFrame({
    'Time Period': ['Commuting Hours', 'Non-Commuting Hours'],
    'Total Ridesharing Trips': [commuting_rideshare_trips.sum(), non_commuting_rideshare_trips.sum()]
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
    chart_worksheet.add_image(chart_image, 'D2')

print(f"Results and chart saved to {result_excel_path}")