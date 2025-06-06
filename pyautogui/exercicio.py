import pyautogui as py
import time


temperature = float(py.prompt('Qual a temperatura?: '))

if temperature <10:
    py.alert('Muito frio')
elif temperature>=10 and temperature<=18:
    py.alert('Frio')
elif temperature >18 and temperature <=26:
    py.alert('Agradável')
elif temperature>26 and temperature<=35:
    py.alert('Quente')
else:
    py.alert('Muito quente')