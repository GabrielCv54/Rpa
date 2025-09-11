import pyautogui as p
import time 

#Funções usadas para manipulação do Whatsapp

def escrever_mensagem():
    contact = str(input('Para qual contato deseja mandar uma mensagem?: ')) 
    position_y = 67
    position_x = 158
    time.sleep(5)
    p.move(position_x,position_y)
    p.click()
    url_zap = p.press('https://web.whatsapp.com/')

escrever_mensagem()