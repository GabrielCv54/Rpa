import pyautogui as p
import time 
import webbrowser as web
from bs4 import BeautifulSoup

""" from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from web_driver.chrome import ChromeDriverManager 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) """


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
    time.sleep(5)
    p.click()
    time.sleep(5)
    p.hotkey('ctrl','t')
    time.sleep(5)
    p.hotkey('ctrl','l')
    time.sleep(5)
    p.write('https://web.whatsapp.com')
    time.sleep(3)
    p.press('enter')
    time.sleep(7)
    p.moveTo(40,200)
    p.click()
    time.sleep(5)
    p.moveTo(186,391)
    p.click()
    while True:
     time.sleep(5)
     p.press('right')
     break
    
    print("Todos os status visualizados com sucesso!✅")

def visualizar_grupos():
    p.moveTo(39,305)
    time.sleep(5)
    p.click()
    time.sleep(6)
    p.moveTo(411,274)
    p.click()
    time.sleep(5)


def adicionar_novo_contato():
    name = str(input('Novo contato: '))
    contact = int(input('Qual o número do telefone?: '))
    """isSurname = str(input(("Deseja colocar sobrenome?: ")))
    if isSurname == 'nao':
        pass
    else:
     surname = str(input('Sobrenome: '))  """

    p.PAUSE = 5
    time.sleep(3)
    p.moveTo(801,1042)
    p.click()
    time.sleep(4.5)
    p.write(name,interval=0.1)
    time.sleep(4)
    p.moveTo(309,479)
    p.click()
    time.sleep(3)
    p.write(contact,interval=0.2)
    time.sleep(3)



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
        adicionar_novo_contato()
    elif what == 6:
        print('Automação Whatsapp finalizada!!!💾✉️')
        
