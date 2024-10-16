import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Best_Actress_Actor.csv'
academy_awards_df = pd.read_csv(file_path)

actor_ages = academy_awards_df['Atores']
actress_ages = academy_awards_df['Atrizes']

actor_bars = actor_ages.value_counts(bins=range(0, 100, 10)).sort_index()
actress_bars = actress_ages.value_counts(bins=range(0, 100, 10)).sort_index()

actor_bars = actor_bars.to_list()
actress_bars = actress_bars.to_list()

actor_bars[0] = actor_bars[0] + actor_bars[1] + actor_bars[2]
actor_bars.pop(1)
actor_bars.pop(1)
actress_bars[0] = actress_bars[0] + actress_bars[1] + actress_bars[2]
actress_bars.pop(1)
actress_bars.pop(1)



labels = ['0-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))
rects1 = ax.bar(x - width/2, actor_bars, width, label='Actors')
rects2 = ax.bar(x + width/2, actress_bars, width, label='Actresses')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Age Groups')
ax.set_ylabel('Counts')
ax.set_title('Counts by age group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()


actress_ages_by_decade = [[], [], [], [], [], [], [], []]
actor_ages_by_decade = [[], [], [], [], [], [], [], []]

for i in range(0,7):
    actress_ages_by_decade[i] = actress_ages[i:i+10].sum() / 10
    actor_ages_by_decade[i] = actor_ages[i:i+10].sum() / 10
actress_ages_by_decade[7] = actress_ages[70:76].sum() / 6
actor_ages_by_decade[7] = actor_ages[70:76].sum() / 6


labels = ['1928-1937', '1938-1947', '1948-1957', '1958-1967', '1968-1977', '1978-1987', '1988-1997', '1998-2003']
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(labels, actress_ages_by_decade, marker='o', label='Actresses')
ax.plot(labels, actor_ages_by_decade, marker='o', label='Actors')

ax.set_xlabel('Decades')
ax.set_ylabel('Average Age')
ax.set_title('Average Age by Decade and Gender')
ax.legend()

fig.tight_layout()

plt.show()