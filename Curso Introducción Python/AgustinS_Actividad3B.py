def tabla_multiplicar(n):
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

tabla_multiplicar(3)
tabla_multiplicar(6)
tabla_multiplicar(9)