# Google Chrome -> chrome driver
# Firefox -> geckodriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Chrome()
# Passo 1: Pegar a cotação do dólar
# entrar no Google
navegador.get("https://www.google.com/")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print (cotacao_dolar)
# Passo 2: Pegar a cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print (cotacao_euro)
# Passo 3: Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")
print (cotacao_ouro)
navegador.quit()
# Passo 4: Importar a base de dados e Atualizar a base
import pandas as pd
tabela = pd.read_excel("Produtos.xlsx")
display (tabela)
# Passo 5: Recalcular os preços
# atualizar a cotação
# cotação dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
# preço de compra = cotação * preço original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
# preço de venda = preço de compra * a margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
display(tabela)
# Passo 6: Exportar a base atualizada
tabela.to_excel("Produtos Novo.xlsx",index=False)
