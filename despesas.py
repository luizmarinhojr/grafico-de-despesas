import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Recebendo o número de dias
while True:
    try:
        dias = int(input('Digite o número de dias: '))
        if dias < 1:
            raise ValueError
        print(f'\nQuantidade de dias: {dias}')
        decisao = int(input('Deseja confirmar? [1] Sim  [2] Não -> '))
        if decisao != 1: raise ValueError
        break
    except ValueError:
        print('\nDigite no mínimo 1 número inteiro')

# Recebendo as categorias de despesas
while True:
    try:
        categorias = list(map(str, input('\nDigite as categorias de despesas separadas por espaço (Ex: Alimentação Transporte): ').split()))
        print('\nCategorias de despesa: ', ', '.join(categorias))
        decisao = int(input('Deseja confirmar? [1] Sim  [2] Não -> '))
        if decisao != 1: raise ValueError
        break
    except ValueError:
        print('\nDigite novamente...')

# Recebendo os valores das despesas por dia
despesasPorDia = {}
while True:
    try:
        for dia in range(1, dias+1):
            despesasPorDia[dia] = {}
            print(f'\nDia {dia}')
            for y in categorias:
                valor = float(input(f'Digite o valor para a categoria {y}: '))
                if valor < 0:
                    raise ValueError
                despesasPorDia[dia][y] = valor
            decisao = int(input('\nDeseja confirmar e avançar para o próximo dia? [1] Sim  [2] Não -> '))
            if decisao != 1: 
                raise ValueError
        break
    except ValueError:
        print('\nDigite apenas números positivos')

for day in range(1, dias+1):
    print(f'\nDia {day}')
    for m in categorias:
        print(f'{m}: R$ {despesasPorDia[day][m]}')


# Transformação dos dados para montar os gráficos
class Dados:
    def transformarDados(self):
        self.categoria = {}
        for a in categorias:
            self.categoria[a] = {}
            for dia in despesasPorDia:
                self.categoria[a][dia] = despesasPorDia[dia][a]
        return self.categoria
    
    def transformarDadosEixoX(self, categoria):
        return np.array(list(categoria)).reshape((-1,1))

    def transformarDadosEixoY(self, categoria):
        return np.array(list(categoria[a] for a in categoria))


class Graficos(Dados):
    def __init__(self):
        self.categoria = super().transformarDados()

    def imprimirGraficoTotal(self):
        legenda = []
        for item in self.categoria:
            xdias = super().transformarDadosEixoX(self.categoria[item])
            ydespesa = super().transformarDadosEixoY(self.categoria[item])
            plt.plot(xdias, ydespesa, marker='.', linewidth=3.5, markersize=17)
            legenda.append(item)
        self.mostrarGrafico('Despesas', legenda)
    
    def mostrarGrafico(self, titulo, legenda):
        plt.title(titulo)
        plt.xlabel('Dia')
        plt.ylabel('Despesas em R$')
        plt.legend(legenda)
        print(f'\nGrafico {titulo} Gerado com sucesso!')
        plt.show()

    def imprimirGraficoRegressao(self):
        for item in self.categoria:
            xdias = super().transformarDadosEixoX(self.categoria[item])
            ydespesa = super().transformarDadosEixoY(self.categoria[item])
            regr = LinearRegression().fit(X=xdias, y=ydespesa)
            previsao = regr.predict(xdias)
            plt.plot(xdias, ydespesa, marker='.', linewidth=3.5, markersize=17)
            plt.plot(xdias, previsao, linewidth=2.0)
            titulo = 'Regressão - ' + item
            titulo_legenda = item + ' - Original'
            legenda = [titulo_legenda, 'Regressão Linear']
            self.mostrarGrafico(titulo, legenda)


despesass = Graficos()
despesass.imprimirGraficoTotal()
despesass.imprimirGraficoRegressao()
