import random

def adivinarNumero():
    numeroSecreto = random.randint(1, 10)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina el número (entre 1 y 10): "))
            intentos += 1

            if intento < 1 or intento > 10:
                print("Por favor, ingresa un número entre 1 y 10.")
                continue

            if intento < numeroSecreto:
                print("El número es mayor")
            elif intento > numeroSecreto:
                print("El número es menor")
            else:
                print(f"¡Felicidades! El número es: {numeroSecreto} y fue adivinado en {intentos} intentos.")
        
        except ValueError:
            print('Entrada no válida. Ingresa un número entero.')


adivinarNumero()

#Observaciones para mejorar: *El programa no se reinicia una vez adivinado el número, es decir, el número seguirá siendo el mismo y los intentos se seguirán acumulando en el contador.