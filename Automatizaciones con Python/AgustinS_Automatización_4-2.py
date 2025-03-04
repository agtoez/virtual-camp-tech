import pyautogui
import time
import os

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(2)

txt = "Hola, este texto fue escrito automáticamente con Python y PyAutoGUI. 🚀"
pyautogui.write(txt, interval=0.05)

pyautogui.hotkey("ctrl", "g")
time.sleep(2)

# Definir ruta de guardado
nombre_archivo = "D:\\Users\\users\\Desktop\\mensaje.txt"

pyautogui.hotkey("alt", "l")
time.sleep(1)

pyautogui.write(nombre_archivo)
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)  
pyautogui.press("left") 
pyautogui.press("enter")
