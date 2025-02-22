#Funciones para validar datos ingresados por el usuario:

def obtener_integer(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def obtener_float(mensaje):
    while True:
        try: 
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número decimal válido (por ejemplo, 1.75).")

def obtener_booleano(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ['sí', 'si']:
            return True
        elif respuesta == 'no':
            return False
        else:
            print("Error: Responda 'Sí' o 'No'.")

nombre = input('Ingrese su nombre:  ').strip()
edad = obtener_integer('Ingrese su edad: ')
altura = obtener_float('Ingrese su altura en metros (por ejemplo, 1.75): ')
mascota = obtener_booleano("¿Tiene mascota? (sí/no): ")

if edad <= 50:
    print(f"¡Hola {nombre}! Tenés {edad} años, medís {altura} metros y es {'cierto' if mascota else 'falso'} que tenés mascota.")
else:
    print(f"¡Hola {nombre}! Tiene {edad} años, mide {altura} metros y es {'cierto' if mascota else 'falso'} que tiene mascota.")
