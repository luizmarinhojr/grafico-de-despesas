import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Recebendo o número de dias
while True:
    try:
        dias = int(input('Digite o número de dias: '))
        if dias < 1:
            raise ValueError
        break
    except ValueError:
        print('Digite no mínimo 1 número inteiro')

# Recebendo as categorias de despesas
while True:
    try:
        categorias = list(map(str, input('Digite as despesas separadas por espaço (Ex: alimentação transporte): ').split()))
        print(categorias)
        break
    except ValueError:
        print('valor errado')

# Recebendo os valores das despesas por dia
despesasPorDia = {}
while True:
    try:
        for dia in range(1, dias+1):
            despesasPorDia[dia] = {item:(float(input(f'Digite o valor para o {dia}ª dia da categoria {item}: '))) for item in categorias}
        break
    except ValueError:
        print('Digite apenas números positivos')

print(despesasPorDia)


class Dados:
    def __init__(self):
        self.categoria = {}

    def transformarDados(self):
        for a in categorias:
            for i in despesasPorDia:
                b = {dia:despesasPorDia[dia][a] for dia in despesasPorDia}
            self.categoria[a] = b
            return self.categoria[a]
    
    def transformarDadosEixoX(self):
        xdias = np.array(list(self.transformarDados()[item])).reshape((-1,1))


categoria = {}
for a in categorias:
    for i in despesasPorDia:
        b = {dia:despesasPorDia[dia][a] for dia in despesasPorDia}
    categoria[a] = b


class Graficos(Dados):
    def __init__(self):
        pass

    def imprimirGrafico(self, categoriaDada):
        for item in categoria:
            xdias = np.array(list(categoriaDada[item])).reshape((-1,1))
            ydespesa = np.array(list(categoriaDada[item][a] for a in categoriaDada[item]))
            print(xdias)
            print(ydespesa)
            plt.plot(xdias, ydespesa, marker='.', markersize=17)
        

# despesa = {1:100, 2:0, 3:0, 4:150, 5:0}
# xdias = np.array(list(alimentacao)).reshape((-1,1))
# ydespesa = np.array([alimentacao[item] for item in alimentacao])
# print(xdias)
# print(ydespesa)

# regr = LinearRegression().fit(X=xdias, y=ydespesa)

# previsao = regr.predict(xdias)
# print(previsao)

filled_marker_style = dict(marker='.', linestyle='-', linewidth=3.5, markersize=17,
                           color='#8ECEE7',
                           markerfacecolor='y',
                           markeredgecolor='#8ECEE7')

despesass = Graficos()
despesass.imprimirGrafico(categoria)
plt.title('Despesas')
plt.xlabel('Dia')
plt.ylabel('Despesas')
legendas = []
for item in categorias:
    legendas.append(f'{item}')
plt.legend(legendas)
plt.show()

# plt.plot(xdias, ydespesa, **filled_marker_style)
# plt.plot(xdias, previsao, linewidth=2, c='b')
# plt.title('Despesas')
# plt.xlabel('Dia')
# plt.ylabel('Despesas')
# plt.legend(['Dados', 'Previsão'])
# plt.show()
