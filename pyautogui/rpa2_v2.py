import pyautogui

#Sem função
'''user = pyautogui.password("Senha : ")

if user == 'Admin'.lower():
    pyautogui.alert('Acesso concedido!!')
else:
    pyautogui.alert('Acesso negado!!')'''


faculdade = 'Impacta'
faculdadeInput = pyautogui.prompt('Qual a faculdade da rua cubatão??: ')
if faculdadeInput == faculdade.lower():
    pyautogui.alert('Meus parabéns você acertou!')
else:
    pyautogui.alert('Errado! É a Faculdade Impacta')

'''
def password():
    user = pyautogui.password("Senha : ")

    if user == 'Admin'.lower():
        pyautogui.alert('Acesso concedido!!')
    else:
        pyautogui.alert('Acesso negado!!')

password()'''