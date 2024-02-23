import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# olavaga = {1:100, 2:0, 3:0, 4:150, 5:0}

# test = np.array(olavaga.items)

# print(test)

# despesa = {1:100, 2:0, 3:0, 4:150, 5:0}
# xdias = np.array(list(despesa)).reshape((-1,1))
# ydespesa = np.array([despesa[item] for item in despesa])
# print(xdias)
# print(ydespesa)

# categorias = {1: 1.0, 2: 5.0, 3: 9.0}
# xdias = np.array(list(categorias)).reshape((-1,1))
# print(xdias)
# for item in categorias:
#     ydespesa = np.array([categorias[a] for a in categorias])
# print(ydespesa)

# plt.plot(xdias, ydespesa, **filled_marker_style)
# # plt.plot(xdias, previsao, linewidth=2, c='b')
# # plt.title('Despesas')
# # plt.xlabel('Dia')
# # plt.ylabel('Despesas')
# # plt.legend(['Dados', 'Previsão'])
# # plt.show()

alimentacao = {1:100, 2:0, 3:0, 4:150, 5:0}
xdias = np.array(list(alimentacao)).reshape((-1,1))
ydespesa = np.array([alimentacao[item] for item in alimentacao])
print(xdias)
print(ydespesa)

# regr = LinearRegression().fit(X=xdias, y=ydespesa)

# previsao = regr.predict(xdias)
# print(previsao)

filled_marker_style = dict(marker='.', linestyle='-', linewidth=3.5, markersize=17,
                           color='#8ECEE7',
                           markerfacecolor='y',
                           markeredgecolor='#8ECEE7')

y = [4,6,8,9,7]
z = [10,12,15,13,42]

plt.plot(xdias,ydespesa, **filled_marker_style)
plt.title('Despesas')
plt.xlabel('Dia')
plt.ylabel('Despesas')
plt.legend(['Dados'])
plt.show()
