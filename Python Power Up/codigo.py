# Passo 1 - Entrar no sistema da empresa
#     Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Pegar/Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5- Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever na tela
# pyautogui.press - aperta 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema
# Abrir o navegador 
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

# Entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

# Passo 2 - Fazer login
pyautogui.click(x=802,y=389)
pyautogui.hotkey("ctrl","a")
pyautogui.write("gamer@gmail.com")

# Passo 3 - Passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("fajnsdçlfjl1j2318273jasldjfs")

pyautogui.click(x=797, y=533)

time.sleep(2)

pyautogui.click(x=762, y=258)

# Passo 3 - Importar banco de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

# Passo 4 - Cadastrar o produto
for linha in tabela.index:  
    # codigo 
    pyautogui.click(x=762, y=260)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    # marca 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    # categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    # preço unitário
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    # preço unitário
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    # obs
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))

    # enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)