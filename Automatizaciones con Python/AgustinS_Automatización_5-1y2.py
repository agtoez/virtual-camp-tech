import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def buscar_en_google(termino):
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    
    search_box = driver.find_element("name", "q")
    search_box.send_keys(termino)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    resultados = driver.find_elements("css selector", "h3")[:5]
    enlaces = driver.find_elements("css selector", "h3 a")[:5]
    
    resultados_lista = []
    for i in range(len(resultados)):
        titulo = resultados[i].text
        enlace = enlaces[i].get_attribute("href")
        resultados_lista.append(f"{titulo} - {enlace}")
    
    driver.quit()
    
    with open("resultados.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(resultados_lista))
    
    return resultados_lista

def scraper_precio(url, selector_precio):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        precio = soup.select_one(selector_precio)
        
        if precio:
            return precio.text.strip()
        else:
            return "No se encontró el precio."
    else:
        return "Error al acceder a la página."

if __name__ == "__main__":
    opcion = input("¿Qué quieres hacer? (1: Buscar en Google, 2: Scraper de precios): ")
    
    if opcion == "1":
        termino = input("Ingresa el término de búsqueda: ")
        resultados = buscar_en_google(termino)
        for res in resultados:
            print(res)
    
    elif opcion == "2":
        url = input("Ingresa la URL del producto: ")
        selector = input("Ingresa el selector CSS del precio: ")
        precio = scraper_precio(url, selector)
        print(f"Precio encontrado: {precio}")
    else:
        print("Opción no válida.")
