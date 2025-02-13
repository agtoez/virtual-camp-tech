nombre = str(input('Ingrese su nombre: '))
edad = int(input('Ingrese su edad: '))
altura = float(input('Ingrese su altura en metros (por ejemplo, 1.75): '))
mascota = (input('¿Tiene mascota? (sí/no) ')).strip().lower() == 'sí'

if edad <= 50:
    print(f"¡Hola {nombre}! Tenés {edad} años, medís {altura} metros y es {'cierto' if mascota else 'falso'} que tenés mascota.")
else:
    print(f"¡Hola {nombre}! Tiene {edad} años, mide {altura} metros y es {'cierto' if mascota else 'falso'} que tiene mascota.")
