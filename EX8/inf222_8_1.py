import random
from random import choice
from math import comb
from scipy.stats import wilcoxon
from scipy.stats import binom
import pandas as pd

print('a.')

valores_atrizes = '''22 37 28 63 32 26
31 27 27 28 30 26
29 24 38 25 29 41
30 35 35 33 29 38
54 24 25 46 41 28
40 39 29 27 31 38
29 25 35 60 43 35
34 34 17 37 42 41
36 32 41 33 31 74
33 50 38 61 21 41
26 80 42 19 33 35
45 49 39 34 26 25
33 35 35 28
'''

valores_atrizes = [int(x) for x in valores_atrizes.split()]
#random_values = random.sample(valores_atrizes, 10)
random_values = [37, 30, 54, 36, 34, 28, 38, 41, 29, 41]
print(random_values)

above = sum(1 for value in random_values if value > 33.5)
print(f"Número de valores acima de 33.5: {above}")

n = 10
print(f"Número de valores da amostra: {n}")

p_maior_33_5 = 1 - binom.cdf(above - 1, n, 0.5)
print(f"P{{S≥{above}}}: {p_maior_33_5}")
p_menor_33_5 = binom.cdf(above, n, 0.5)
print(f"P{{S≤{above}}}: {p_menor_33_5}")

valor_p = 2 * min(p_maior_33_5, p_menor_33_5)
print(f"Valor p: {valor_p}")

#--------------------------------------------
# b.

print('-'*20)
print('b.')

random_values = [value - 33.5 for value in random_values]
random_values.sort(key=abs)

print(f"Distancias ordenadas: {random_values}")
postos = [1, 2, 3.5, 3.5, 5.5, 5.5, 7, 8.5, 8.5, 10]
print(f"Postos: {postos}")

W = [postos[k] for k in range(n) if random_values[k] > 0]
W = sum(W)
print(f"Valor de W: {W}")

stat, p_menor_W = wilcoxon(random_values)
print(f"P{{W≤{W}}}: {p_menor_W}")
p_maior_W = 1 - p_menor_W
print(f"P{{W≥{W}}}: {p_maior_W}")
valor_p = 2 * min(p_maior_W, p_menor_W)
print(f"Valor p: {valor_p}")


#--------------------------------------------
# c.

print('-'*20)
print('c.')

valores_atores ='''
44 41 62 52 41 34
34 52 41 37 38 34
32 40 43 56 41 39
49 57 41 38 42 52
51 35 30 39 41 44
49 35 47 31 47 37
57 42 45 42 44 62
43 42 48 49 56 38
60 30 40 42 36 76
39 53 45 36 62 43
51 32 42 54 52 37
38 32 45 60 46 40
36 47 29 43
'''

valores_atores = [int(x) for x in valores_atores.split()]
#random_values_atores = random.sample(valores_atores, 10)
random_values_atores = [36, 52, 40, 43, 44, 41, 57, 56, 62, 52]
print(random_values_atores)
#random_values_atrizes = random.sample(valores_atrizes, 10)
random_values_atrizes = [26, 74, 38, 21, 38, 32, 27, 25, 41, 29]
print(random_values_atrizes)

random_values_atores.sort()
random_values_atrizes.sort()

print(f"valores_atores ordenado: {random_values_atores}")
print(f"valores_atrizes ordenado: {random_values_atrizes}")

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

merged, merged_from = merge(random_values_atores, random_values_atrizes, 10)


for i, value in enumerate(merged):
    if merged_from[i] == '0':
        print(f"\033[4m{value}\033[0m", end=' ')
    else:
        print(value, end=' ')
print()


U = 0
for i in range(20):
    if merged_from[i] == '0':
        U += i + 1

print(f"U: {U}")







