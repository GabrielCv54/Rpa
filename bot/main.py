import pyautogui as p
import webbrowser
import time
import pandas as pd

csv_file = pd.read_excel('bot/contatos/contatos_zap.xlsx')
print(csv_file)

csv_dict = csv_file.to_dict('list')

contatos = csv_dict['Telefone']
message = csv_dict['mensagem']
combo = zip(contatos[0],message[0])
first = True
for cont,mess in combo:
    time.sleep(5)
    webbrowser.open('https://web.whatsapp.com/send?phone='+cont+"&text="+mess)
    if first:
        time.sleep(6)
        first = False

    width,height = p.size()
    p.click(width/2,height/2)
    time.sleep(5)
    p.press('esc')
    time.sleep(6)
    p.press('enter')
    time.sleep(7)
    p.hotkey('ctrl','w')