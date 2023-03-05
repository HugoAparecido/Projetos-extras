# Passo a passo de um projeto de ciência de dados
# Passo 1: Entendimento do desafio
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção de Dados
# Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# Passo 5: Análise Exploratória
# Passo 6: Modelagem + Algoritmos(Aqui que entra a Inteligência Artificial se necessário)
# Passo 7: Interpretação de Resultados
# importar a base de dados
import pandas as pd
tabela = pd.read_csv("advertising.csv")
display(tabela)
print(tabela.info())
# Análise Exploratória
import matplotlib.pyplot as plt
import seaborn as sns
# criar um gráfico
sns.heatmap(tabela.corr(),cmap="Greens",annot=True)
# exibe o gráfico
plt.show()
# matplotlib
# seaborn
# Separando entre dados de venda e dados de teste
y = tabela["Vendas"]
x = tabela[["TV","Radio","Jornal"]]
x = tabela.drop["Vendas"]
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)
# Regressão Linear
# RandomForest(Árvore de Decisão)
# importar a inteligência artificial
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
# criar a inteligência artificial
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()
# treinar a inteligência artificial
modelo_regressaolinear.fit(x_treino,y_treino)
modelo_arvoredecisao.fit(x_treino,y_treino)
# Teste da AI e Avaliação do Melhor Modelo
# Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece
previsao_regressaolinear=modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
from sklearn.metrics import r2_score
print(r2_score(y_teste,previsao_regressaolinear))
print(r2_score(y_teste,previsao_arvoredecisao))
# Visualização Gráfica das Previsões
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Precisao Arvore Decisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsao RegressaoLinear"] = previsao_regressaolinear
sns.lineplot(data=tabela_auxiliar)
plt.show()
# Como fazer uma nova precisão?
nova_tabela = pd.read_csv("novos.csv")
display(nova_tabela)
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)
#!pip install matplotlib
#!pip install seaborn
#!pip install scikit-learn
