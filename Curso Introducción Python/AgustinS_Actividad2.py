def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else: 
        return "Obesidad"

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
categoría = clasificar_imc(imc)

print(f"Tu IMC es {imc:.1f} y tu clasificación es: {categoria}.")