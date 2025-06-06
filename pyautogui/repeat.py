import pyautogui as py
import time 
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8')

for i in range(1,11):
    time.sleep(0.5)
    py.alert(f'Número do laço : {i}')
    print(i)