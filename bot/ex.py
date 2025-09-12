import pyautogui as p
import time 

#Funções usadas para manipulação do Whatsapp

contact = str(input('Para qual contato deseja mandar uma mensagem?: ')) 
message = str(input('Digite a mensagem aqui: '))


def escrever_mensagem(cont,mess):
    position_y = 67
    position_x = 158
    p.position(position_x,position_y)
    #p.move(position_x,position_y)
    time.sleep(15)
    p.click()
    time.sleep(10)
    p.press('https://web.whatsapp.com/')
    time.sleep(20)
    p.press('enter')
    time.sleep(20)
    p.press('https://web.whatsapp.com/send?name='+contact+'&text='+message)


def trocar_foto():
    x = 29
    y = 951
    

def ver_status():
    pass

def visualizar_grupos():
    pass


escrever_mensagem(cont=contact,mess=message)