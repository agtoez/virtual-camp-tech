import pyautogui
import time
import os

app_name = input("Ingrese el nombre de la aplicación a abrir: ")
intervalo_captura = int(input("Ingrese el intervalo de captura en segundos: "))

def abrir_app(nombre_app):
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write(nombre_app)
    pyautogui.press("enter")
    time.sleep(3)

carpeta_capturas = "capturas"
os.makedirs(carpeta_capturas, exist_ok=True)

def tomar_capturas():
    for i in range(5):
        captura = pyautogui.screenshot()
        nombre_archivo = os.path.join(carpeta_capturas, f"captura_{i+1}.png")
        captura.save(nombre_archivo)
        print(f"Captura guardada: {nombre_archivo}")
        time.sleep(intervalo_captura)

abrir_app(app_name)
tomar_capturas()

print("Proceso completado.")
