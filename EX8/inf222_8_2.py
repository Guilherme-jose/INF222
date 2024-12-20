#--------------------------------------------
# 2.a.

import pandas as pd


data = pd.read_csv('/home/guilherme/INF222/EX8/dados.csv')
print(data.head())

data_2018 = data[['País', '2018']]

paises_america_do_sul = [
    'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 
    'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela'
]

data_south_america = data_2018[data_2018['País'].isin(paises_america_do_sul)]
data_south_america = data_south_america.sample(10)
print(data_south_america)

data_south_america = data_south_america['2018']
data_south_america = data_south_america.to_list()
data_south_america = [data_south_america[i] - 2 for i in range(10)]
data_south_america.sort(key=abs)
data_south_america = [round(num, 4) for num in data_south_america]

print(f"distancias ordenadas: {data_south_america}")

W = 0
for i in range(10): 
    if data_south_america[i] > 0:
        W += i + 1

print(f"W: {W}")

#--------------------------------------------
# 2.b.

paises_europa = [
    'Albânia', 'Alemanha', 'Andorra', 'Armênia', 'Áustria', 'Azerbaijão', 'Bélgica', 'Bielorrússia', 
    'Bósnia e Herzegovina', 'Bulgária', 'Chipre', 'Croácia', 'Dinamarca', 'Eslováquia', 'Eslovênia', 
    'Espanha', 'Estônia', 'Finlândia', 'França', 'Geórgia', 'Grécia', 'Hungria', 'Irlanda', 'Islândia', 
    'Itália', 'Kosovo', 'Letônia', 'Liechtenstein', 'Lituânia', 'Luxemburgo', 'Macedônia do Norte', 
    'Malta', 'Moldávia', 'Mônaco', 'Montenegro', 'Noruega', 'Países Baixos', 'Polônia', 'Portugal', 
    'Reino Unido', 'República Tcheca', 'Romênia', 'Rússia', 'San Marino', 'Sérvia', 'Suécia', 'Suíça', 
    'Turquia', 'Ucrânia', 'Vaticano'
]


data_europe = data_2018[data_2018['País'].isin(paises_europa)]
data_europe = data_europe.sample(10)
print(data_europe)

data_europe = data_europe['2018']
data_europe = data_europe.to_list()
data_europe = [data_europe[i] - 2 for i in range(10)]
data_europe.sort(key=abs)
data_europe = [round(num, 4) for num in data_europe]
print(f"distancias ordenadas: {data_europe}")

W = 0
for i in range(10): 
    if data_europe[i] > 0:
        W += i + 1

print(f"W: {W}")

#--------------------------------------------
# 2.c.
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

paises_america_do_sul = [
    'Guiana', 'Paraguai', 'Venezuela', 'Uruguai', 'Colômbia', 
    'Peru', 'Peru', 'Equador', 'Brasil', 'Suriname'
]

data_south_america = data_2018[data_2018['País'].isin(paises_america_do_sul)]
data_south_america = data_south_america['2018'].tolist()

paises_europa = [
    'Albânia', 'Grécia', 'Rússia', 'Lituânia', 'França', 
    'Azerbaijão', 'Suíça', 'Geórgia', 'Andorra', 'Suécia'
]

data_europe = data_2018[data_2018['País'].isin(paises_europa)]
data_europe = data_europe['2018'].tolist()

data_south_america.sort()
data_europe.sort()

print(f"valores ordenados america do sul: {data_south_america}")
print(f"valores ordenados europa: {data_europe}")

merged, merged_from = merge(data_south_america, data_europe, 10)


print(f"Merged: {merged}")
print(f"Merged from: {merged_from}")


U = 0
for i in range(20):
    if merged_from[i] == '0':
        U += i + 1

print(f"U: {U}")




#--------------------------------------------
# 2.d.
'''
paises_africa = [
    'África do Sul', 'Angola', 'Argélia', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 
    'Camarões', 'Chade', 'Comores', 'Congo', 'Costa do Marfim', 'Djibouti', 'Egito', 'Eritreia', 'Eswatini', 
    'Etiópia', 'Gabão', 'Gâmbia', 'Gana', 'Guiné', 'Guiné-Bissau', 'Guiné Equatorial', 'Lesoto', 'Libéria', 
    'Líbia', 'Madagáscar', 'Malawi', 'Mali', 'Marrocos', 'Maurícia', 'Mauritânia', 'Moçambique', 'Namíbia', 
    'Níger', 'Nigéria', 'Quênia', 'República Centro-Africana', 'República Democrática do Congo', 'Ruanda', 
    'São Tomé e Príncipe', 'Senegal', 'Serra Leoa', 'Seychelles', 'Somália', 'Sudão', 'Sudão do Sul', 
    'Tanzânia', 'Togo', 'Tunísia', 'Uganda', 'Zâmbia', 'Zimbábue'
]

data_africa = data_2018[data_2018['País'].isin(paises_africa)]
data_africa = data_africa.sample(10)
print(data_africa)

data_africa = data_africa['2018']
data_africa = data_africa.to_list()
data_africa.sort()
'''

paises_africa = [
    'África do Sul', 'Serra Leoa', 'Costa do Marfim', 'Nigéria', 'Tanzânia', 
    'Uganda', 'Congo', 'Somália', 'Sudão do Sul', 'Mauritânia'
]

data_africa = data_2018[data_2018['País'].isin(paises_africa)]
data_africa = data_africa['2018'].tolist()

print(f"valores ordenados africa: {data_africa}")

merged, merged_from = merge(data_south_america, data_africa, 10)

print(f"Merged: {merged}")
print(f"Merged from: {merged_from}")

U = 0
for i in range(20):
    if merged_from[i] == '1':
        U += i + 1

print(f"U: {U}")


