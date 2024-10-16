import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



file_path = 'PIB per capita - SouthAmerica.csv'
pib_per_capita_df = pd.read_csv(file_path)

  

pib_per_capita_df.rename(columns={'GDP per capita, current prices\r\n (U.S. dollars per capita)': 'countries'}, inplace=True)

pib_per_capita_df = pib_per_capita_df.replace('no data', np.nan)
pib_per_capita_df.iloc[:, 1:] = pib_per_capita_df.iloc[:, 1:].replace(',', '.', regex=True)
pib_per_capita_df.iloc[:, 1:] = pib_per_capita_df.iloc[:, 1:].astype(float)




years = pib_per_capita_df.columns[1:].astype(int)
fig, ax = plt.subplots(figsize=(12, 8))


for country in pib_per_capita_df['countries']:
    country_data = pib_per_capita_df[pib_per_capita_df['countries'] == country].iloc[0, 1:]
    ax.plot(years, country_data, marker='o', label=country)

ax.set_xlabel('Year')
ax.set_ylabel('GDP per capita (U.S. dollars)')
ax.set_title('GDP per capita over the years for South American countries')
ax.legend()

fig.tight_layout()
plt.show()


# Sort the DataFrame by the GDP per capita in 2024 and select the top 10 countries
top_countries = pib_per_capita_df.sort_values(by='2024', ascending=False).head(5)

fig, ax = plt.subplots(figsize=(12, 8))

for country in top_countries['countries']:
    country_data = top_countries[top_countries['countries'] == country].iloc[0, 1:]
    ax.plot(years, country_data, marker='o', label=country)

ax.set_xlabel('Year')
ax.set_ylabel('GDP per capita (U.S. dollars)')
ax.set_title('Top 5 South American countries by GDP per capita in 2024')
ax.legend()

fig.tight_layout()
plt.show()

