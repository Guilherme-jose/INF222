import matplotlib.pyplot as plt

# Valores fornecidos
x = [0, 1, 2]
y = [0.56, 0.94, 1]

# Desenhar a FDA
plt.plot(x, y, marker='o')

# Configurações do gráfico

plt.ylim(bottom=0)
plt.title('Função de Distribuição Acumulada (FDA)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)

# Mostrar o gráfico
plt.show()