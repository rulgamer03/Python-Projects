import pyautogui

#Podemos escribir cadenas de texto directamente
pyautogui.typewrite('Hola mundo!')

#Podemos escribir listas de caracteres individuales b
letras=['r','a','u','l','c','c','a','r']
pyautogui.typewrite(letras)

#Tambien podemos presionar las teclas de direccion
posicion = ['a','up','b','down','c','left','d','right']
pyautogui.typewrite(posicion)

pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')



