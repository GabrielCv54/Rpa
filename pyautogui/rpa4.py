import time
import pyautogui

status = 'pendente'
while status == 'pendente':
    print('Aguardando aprovação!!!')
    time.sleep(4)#tempo de espera
    #simulando mudança de estado
    status = 'aprovado'

print("Processo Aprovado! Continuando automação!")