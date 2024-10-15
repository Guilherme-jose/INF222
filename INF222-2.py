import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Best_Actress_Actor.csv'
academy_awards_df = pd.read_csv(file_path)

print(academy_awards_df.head())

academy_awards_df.hist(bins=range(30,80,5), figsize=(15, 10), edgecolor='black')

plt.suptitle('Histograms of Academy Awards Data', fontsize=16)

plt.show()


