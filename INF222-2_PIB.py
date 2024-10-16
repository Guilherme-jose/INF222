import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file_path = 'PIB - SouthAmerica.csv'
pib_df = pd.read_csv(file_path)

pib_df.rename(columns={'GDP, current prices (Billions of U.S. dollars)': 'countries'}, inplace=True)


PIB_2024 = pib_df[['countries', '2024']]
PIB_2024 = PIB_2024.replace('no data', np.nan).dropna()

PIB_2024.iloc[:, 1] = PIB_2024.iloc[:, 1].str.replace(',', '')
PIB_2024.iloc[:, 1] = PIB_2024.iloc[:, 1].astype(float)

threshold = 2
total_pib = PIB_2024['2024'].sum()
PIB_2024['percentage'] = (PIB_2024['2024'] / total_pib) * 100

PIB_2024 = PIB_2024[PIB_2024['percentage'] >= threshold]

others_PIB = total_pib - PIB_2024['2024'].sum()

PIB_2024 = pd.concat([PIB_2024, pd.DataFrame([{'countries': 'Others', '2024': others_PIB, 'percentage': (others_PIB / total_pib) * 100}])], ignore_index=True)

PIB_2024 = PIB_2024.sort_values(by='2024', ascending=False)


fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(PIB_2024['2024'], labels=PIB_2024['countries'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax.set_title('PIB Distribution for 2024')

plt.show()