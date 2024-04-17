
import matplotlib.pyplot as plt 

categorias=['Janeiro','Fevereiro','Março','Abril']
valores=[20,30,60,80]

#criar o gráfico de colunas
bars=plt.bar(categorias, valores)

#adicionar os rótulos de valores
plt.bar_label(bars, labels=valores,label_type='edge')

#adicionar os rótulos de categoria
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Valores de Vendas do Semestre')

#mostrar o gráfico
plt.show()

#biblioteca online com gráficos diversos https://matplotlib.org/stable/plot_types/index.html