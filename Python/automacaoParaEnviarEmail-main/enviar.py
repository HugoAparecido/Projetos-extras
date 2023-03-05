# Para baixar a biblioteca pyautogui
#pip install pyautogui
# Para baixar a biblioteca pyautogui no Jupyter
#!pip install pyautogui
import pyautogui
import pyperclip
import time
# pyautogui.click -> clicar
# pyautogui.Write -> escrever
# pyautogui.press -> pressionar
# pyautogui.hotkey -> atalhos
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
# Passo 1: Entar no sitema da empresa (no link do drive)
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://drive.google.com/drive/u/0/folders/18lPOmfvu40Wt0xeXiuJRmnqJ7mWcEx4P")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
# Passo 2: Navegar até o local do relatório (entrar na pasta exportar)
pyautogui.click(x=484, y=377, clicks=2)
# Para descobrir a posição do item que você queira clicar
#import time
#time.sleep(5)
#print(pyautogui.position())
time.sleep(2)
# Passo 3: Exportar o relatório (fazer o download)
pyautogui.click(x=486, y=475)
pyautogui.click(x=1672, y=240)
pyautogui.click(x=1448, y=749)
time.sleep(5)
# Passo 4: Calcular os indicadores (faturamento e quantidade de produtos)
# A biblioteca tabula permite que o pandas leia arquivo pdf
import pandas as pd
# Se  não for no jupyter tem que instalar o pandas, numpy, openpyxl
tabela = pd.read_excel(r"C:\Users\Hugo\Downloads\Vendas - Dez.xlsx")
display(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)
# Passo 5: Enviar um e-mail para a diretoria
# abrir aba e entrar no e-mail
pyautogui.hotkey("ctrl","t") # abre a aba
pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
# clicar no botão escrever
pyautogui.click(x=105, y=262)
# preencher as informações do e-mail
# destinatário
pyautogui.write("hugoapga626@gmail.com")
pyautogui.press("tab") # seleciona o e-mail
pyautogui.press("tab") # pula para o campo de assunto
# assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
# corpo
texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade}
    
Abs
HugoAp"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")
