import pyautogui as pt
import pyperclip
import time

# Línea desde la cual comenzar a leer (índice basado en 0)
start_line = 251  # Cambia esto al número de línea deseado
stop_line = 265
  # Cambia esto al número de línea donde deseas detener el proceso

# Tiempo de espera inicial
time.sleep(3)

# Abrir el archivo de texto con la lista de correos electrónicos
with open('correos.txt', 'r') as file:
    emails = file.readlines()

# Recorrer la lista de correos electrónicos y enviar los mensajes
for i in range(start_line - 1, len(emails)):
    email = emails[i].strip() + "@uninorte.edu.co"  # Agregar el dominio
    pyperclip.copy(email)  # Copiar el correo electrónico al portapapeles
    pt.hotkey('ctrl', 'v')  # Pegar el correo desde el portapapeles
    time.sleep(2)  # Agregar un tiempo de espera antes de pegar el siguiente correo
    pt.press("enter")
    time.sleep(2)  # Agregar un tiempo de espera antes de pegar el siguiente correo
    
    if i == stop_line - 1:
        break  # Salir del bucle cuando alcance la línea deseada
