#Consigna:
# Crea una función llamada calcular_imc(peso, altura) que reciba como parámetros el peso en kilogramos y la altura en metros, y devuelva el Índice de Masa Corporal (IMC).

def calcular_imc(peso, altura):
    if peso <= 0:
        return "El peso no puede ser menor que 0."
    elif altura <= 0:
        return "La altura no debe ser menor que 0."
    else:
        return peso / (altura ** 2)

#Consigna:
#Crea otra función llamada clasificar_imc(imc) que reciba el valor del IMC y devuelva un mensaje con la categoría correspondiente.

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else: 
        return "Obesidad"

# En el programa principal:

#     Solicita al usuario su peso (float) y altura (float).
#     Usa las funciones creadas para calcular y clasificar el IMC.
#     Muestra un mensaje con el resultado, por ejemplo:
#         Tu IMC es 23.1 y tu clasificación es: Peso normal.


peso = float(input("Ingrese su peso en kg, (por ejemplo 70): "))
altura = float(input("Ingrese su altura en metros, (por ejemplo 1.75): "))

imc = calcular_imc(peso, altura)
categoría = clasificar_imc(imc)

print(f"Tu IMC es de: {imc:.1f} y su clasificación es: {categoría}.")