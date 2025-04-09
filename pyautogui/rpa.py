'''Abrir o bloco de notas e digitar qualquer coisa'''

import os
import pyautogui
import time
from datetime import datetime

#Define pausa de 2 segundos entre cada comando
pyautogui.PAUSE = 2

#Se tiver  algo aberto no bloco de notas ,é fechado
os.system('taskkill /f /im notepad.exe')

#Aguarda para garantir que o arquivo foi fechado
time.sleep(2)

#Abrir o menu iniciar do windows
pyautogui.press("win")

#Pesquisar bloco de notas e pressionar a tecla Enter
pyautogui.write('bloco de notas',interval=0.2)
pyautogui.press('Enter')

#Aguardar abrir o bloco de notas
time.sleep(2)

#Abrir uma nova aba no bloco de notas
pyautogui.hotkey('ctrl','n')

#aguarda para saber se uma nova aba abriu
time.sleep(1)

#Começar a digitar no bloco de notas
pyautogui.write('Academia*12',interval=0.2)

#Salvar o arquivo(CTRL + S)
pyautogui.hotkey('ctrl',"s")

#abir a caixa de diálogo "Salvar como" usando F12
pyautogui.hotkey('ctrl','shift','s')


#aguardar a abertura da caixa de diálogos salvar
time.sleep(1)

#informar o nome do arquivo para salvar
name_archive = datetime.now().strftime("senha_docker")
pyautogui.write(name_archive)

#Pressionar a tecla Enter para salvar
pyautogui.press('Enter')

#Aguadar para garantir que o arquivo foi salvo
time.sleep(2)

#Fechar o bloco de notas
pyautogui.hotkey('alt','f4')

#garantir que o processo foi encerrado
time.sleep(1)
os.system('taskkill/f /im notepad.exe')


print(f'Deu tudo certo , o arquivo foi salvo como {name_archive} !!')
