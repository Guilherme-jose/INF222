import pandas as pd

df = pd.read_csv('dados.csv')

random_countries = df['País'].sample(n=10)
selected_data = df[df['País'].isin(random_countries)][['País', '2010', '2018']]
print(selected_data)
selected_data = selected_data.dropna()

data_2010 = selected_data['2010'].tolist()
data_2018 = selected_data['2018'].tolist()

data_2010.sort()
data_2018.sort()

def merge(a, b, size):
    merged_from = []
    merged = []
    count_a = 0
    count_b = 0
    for i in range(2 * size):
        if count_a == size:
            merged.append(b[count_b])
            merged_from.append('1')
            count_b += 1
        elif count_b == size:
            merged.append(a[count_a])
            merged_from.append('0')
            count_a += 1
        elif a[count_a] < b[count_b]:
            merged.append(a[count_a])
            merged_from.append('0')
            count_a += 1
        else:
            merged.append(b[count_b])
            merged_from.append('1')
            count_b += 1
    
    return merged, merged_from

merged, merged_from = merge(data_2010, data_2018, 10)
print(f"Merged: {merged}")
print(f"Merged from: {merged_from}")

U = 0
for i in range(20):
    if merged_from[i] == '1':
        U += i + 1

print(f"U: {U}")

#-------------------------
# b.
n = 10

random_countries = df['País'].sample(n)
selected_data = df[df['País'].isin(random_countries)][['País', '2010']]
print(selected_data)
data_2010 = selected_data['2010'].tolist()

random_countries = df['País'].sample(n)
selected_data = df[df['País'].isin(random_countries)][['País', '2018']]
print(selected_data)
data_2018 = selected_data['2018'].tolist()

merged, merged_from = merge(data_2010, data_2018, n)
print(f"Merged: {merged}")
print(f"Merged from: {merged_from}")

U = 0
for i in range(2*n):
    if merged_from[i] == '1':
        U += i + 1

print(f"U: {U}")



