import pandas as pd# Se não for no Jupyter, terá que instalar antes o pandas, o numpy e o openpyxl
# Passo 1: Importaria a base de dados
tabela = pd.read_csv("telecom_users.csv")
# Passo 2: Visualizar a base de dados
# - Enterder as informções que você tem disponível
# - Descobrir as cagadas da base de dados
# axis -> 0 = linha; axis -> 1 = coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
# Passo 3: Tratamento de dados
# resolver os valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# resolver valores vazios
# colunas em que TODOS os valores são vazios, eu vou excluir
# axis -> 0 = linha; axis -> 1 = coluna
tabela = tabela.dropna(how="all",axis=1)
# linhas que tenha PELO MENOS 1 valor vazio (que possuem ALGUM valor vazio)
tabela = tabela.dropna(how="any",axis=0)
print(tabela.info())
# Passo 4: Análise Inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
#pip install plotly
# Passo 5: Análise detalhada - descobrir as causas do cancelamento
# comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px
# cria o gráfico
# para cada coluna da minha tabela, eu quero criar um gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # exibe o gráfico
    grafico.show()
