# Gerador de Gráficos de Séries Temporais e Regressão Linear
Esse programa recebe despesas por dia e categoria e gera os gráficos da série temporal (Dias X Valor Despesa), e Regressão Linear (Dias X Valor Despesa) separadamente para cada categoria de despesa.

<br>

## 1 - ENTRADA DE DADOS

#### 1ª ETAPA
1. Usuário digita o número de dias a serem adicionados
2. Programa verifica se o número de dias digitado é maior que zero, caso não, pede que insira novamente
3. O algorítmo solicita confirmação para avançar

#### 2ª ETAPA
1. Usuário entra com o nome das categorias das depesas separados com espaço
2. O algorítmo solicita confirmação para avançar

#### 3ª ETAPA
1. Usuário entra com o valor por dia para cada categoria
2. O algorítmo verifica se o valor digitado para cada dia e categoria é maior que zero, caso não, pede que insira novamente
3. O algorítmo solicita confirmação para avançar

<br>

## 2 - Classe de Despesas (transformação dos dados)
Classe para transformação dos dados para compatibilidade com o método de entrada solicitado pelo Matplotlib.

<br>

## 3 - Classe de Gráficos e Exibição dos gráficos

Chama a classe de Dados para recebimento dos valores das despesas, e em seguida a exibição dos gráficos.
