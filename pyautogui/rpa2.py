import os
import pyautogui


arquivo ='dados.csv'

if os.path.exists(arquivo):
    #código para realizar algum processamento
    pyautogui.alert('Arquivo encontrado👍')
else:
    pyautogui.alert('Arquivo não encontrado!')