
import matplotlib.pyplot as plt 
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho']
valores=[1717,1313,2121,2424,5656,1111]

plt.plot(meses,valores)
plt.xlabel('Meses')
plt.ylabel('Valores')
plt.title('Valores de Vendas do Semestre')

plt.show()
