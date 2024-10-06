def media(valores):
    return sum(valores) / len(valores)

def mediana(valores):
    valores.sort()
    n = len(valores)
    if n % 2 == 0:
        return (valores[n//2 - 1] + valores[n//2]) / 2
    else:
        return valores[n//2]
    
def moda(valores):
    frequencias = {}
    for valor in valores:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1
    moda = max(frequencias, key=frequencias.get)
    return moda

def ponto_medio(valores):
    return (max(valores) + min(valores)) / 2

def amplitude(valores):
    return max(valores) - min(valores)

def desvo_padrao(valores):
    return variancia(valores) ** 0.5

def variancia(valores):
    media_valores = media(valores)
    return sum([(x - media_valores) ** 2 for x in valores]) / len(valores)

def coeficiente_variacao(valores):
    return (desvo_padrao(valores) / media(valores)) * 100

valores_ator = '''44 41 62 52 41 34
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
36 47 29 43'''

valores_ator = [int(x) for x in valores_ator.split()]

print('Média:', media(valores_ator))
print('Mediana:', mediana(valores_ator))
print('Moda:', moda(valores_ator))
print('Ponto médio:', ponto_medio(valores_ator))
print('Amplitude:', amplitude(valores_ator))
print('Desvio padrão:', desvo_padrao(valores_ator))
print('Variância:', variancia(valores_ator))
print('Coeficiente de variação:', coeficiente_variacao(valores_ator))