dados_atrizes = [26, 74, 38, 21, 38, 32, 27, 25, 41, 29]
dados_atores = [36, 52, 40, 43, 44, 41, 57, 56, 62, 52]

import matplotlib.pyplot as plt

plt.boxplot([dados_atrizes, dados_atores], labels=['Atrizes', 'Atores'])
plt.title('Boxplot das Idades de Atrizes e Atores')
plt.ylabel('Idade')
plt.show()

dados_america = [1.02, 1.53, 1.64, 1.96, 1.99, 2.02, 2.99, 3.13, 3.23, 5.17]
dados_europa = [0.18, 0.5, 0.5, 0.51, 0.74, 0.95, 1.06, 1.08, 1.24, 2.38]
dados_africa = [7.15, 13.34, 23.39, 25.36, 47.86, 34.29, 48.9, 37.13, 15.92, 13.75]

plt.boxplot([dados_america, dados_europa, dados_africa], labels=['América', 'Europa', 'África'])
plt.title('Boxplot dos Dados de América, Europa e África')
plt.ylabel('Valores')
plt.show()