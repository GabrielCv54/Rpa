import pyautogui

#Sem função
'''user = pyautogui.password("Senha : ")

if user == 'Admin':
    pyautogui.alert('Acesso concedido!!')
else:
    pyautogui.alert('Acesso negado!!')'''


def password():
    user = pyautogui.password("Senha : ")

    if user == 'Admin'.lower():
        pyautogui.alert('Acesso concedido!!')
    else:
        pyautogui.alert('Acesso negado!!')

password()