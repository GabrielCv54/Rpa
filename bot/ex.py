import pyautogui as p
import time 
import webbrowser as web
import openpyxl as op
""" from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)"""


# ---- Funções usadas para manipulação do Whatsapp


def escrever_mensagem():
    contact = str(input('Para qual contato deseja mandar uma mensagem?: '))
    message = str(input('Digite a mensagem aqui: '))
    link_zap = ('https://web.whatsapp.com')
    #posições da barra de pesquisas
    position_y = 67
    position_x = 158
    p.moveTo(position_x,position_y)
    p.click()
    time.sleep(5)
    p.write(link_zap)
    p.press('enter')
    time.sleep(5)
    p.moveTo(255,213)
    p.click()
    time.sleep(5)
    p.write(contact)
    p.press('enter')
    time.sleep(5)
    p.moveTo(818,985)
    p.click()
    time.sleep(3)
    p.write(message)
    time.sleep(3)
    p.press('enter')
    print('Mensagem foi enviada com sucesso!✅')
    # continue a escrita partir de aqui


def trocar_foto():
     p.moveTo(803,266)
     time.sleep((3))
     p.click()
     p.hotkey('ctrl','t')
     time.sleep(5)
     p.write('https://web.whatsapp.com')
     time.sleep(5)
     p.press('enter')
     time.sleep(5)
     p.click()
     time.sleep(7)
     p.moveTo(40,984)
     p.click()
     time.sleep(5)
     p.moveTo(301,282)
     time.sleep(5)
     p.click()
     p.moveTo(458,424)
    

def ver_status():
    p.moveTo(39,305)
    time.sleep(7)
    p.click()
    time.sleep(5)
    p.moveTo(168,396)
    p.click()
    while True:
     p.press('right')

def visualizar_grupos():
    pass

if __name__ == '__main__':
    what = int(input('O que se deseja fazer?: '))
    if what == 1:
       escrever_mensagem()
    elif what == 2:
        trocar_foto()
    elif what == 3:
        ver_status()
    elif what == 4:
        visualizar_grupos()
    elif what == 5:
        pass

""" print(__name__) """