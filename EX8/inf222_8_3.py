import pandas as pd

print('3.a.')

df = pd.read_csv('dados.csv')

df.dropna(inplace=True)

random_countries = df['País'].sample(n=10)
selected_data = df[df['País'].isin(random_countries)][['País', '2010', '2018']]
print(selected_data)

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

for i, value in enumerate(merged):
    if merged_from[i] == '1':
        print(f"\033[4m{value}\033[0m", end=' ')
    else:
        print(value, end=' ')
print()

U = 0
for i in range(20):
    if merged_from[i] == '1':
        U += i + 1

print(f"U: {U}")

#-------------------------
# b.

print('-'*20)
print('b.')

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

for i, value in enumerate(merged):
    if merged_from[i] == '1':
        print(f"\033[4m{value}\033[0m", end=' ')
    else:
        print(value, end=' ')
print()

U = 0
for i in range(2*n):
    if merged_from[i] == '1':
        U += i + 1

print(f"U: {U}")



