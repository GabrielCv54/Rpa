import pyautogui
import time


#Definir a área inicial do clique
#area_x1,area_y1 : Canto superior esquerdo da área
#area x2,area_y2 : Canto inferior direito da área
area_x1 = 500
area_y1 = 300

area_x2 = 600
area_y2 = 400

print('Mova o cursor dentro da área ')

while True:
    x, y = pyautogui.position() #captura posição do Mouse

    #Verificar se o cursor está dentro da área
    if area_x1 <= x <=area_x2 and area_y1 <= y <= area_y2:
        pyautogui.click(x,y)
        print(f"Clique automático : X = {x}, y ={y}")
        time.sleep(2)
    else:
        print(f"Cursor fora da área: x={x}, y={y}")
    

    time.sleep(1.5)

