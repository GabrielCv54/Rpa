import os 
import pyautogui

directory = "C:/Users/Gabriel/Documents"

for archive in os.listdir(directory):
    print(f'Processando : {archive}')
 
pyautogui.alert('Processo Feito!!')