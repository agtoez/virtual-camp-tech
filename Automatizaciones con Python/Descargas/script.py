"""
📌 Explicación:

pd.DataFrame(data) convierte un diccionario en un DataFrame.
df.to_excel("datos_guardados.xlsx", index=False) guarda el DataFrame sin la columna de índice.
"""

import pandas as pd

# Crear un DataFrame con datos
data = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Madrid", "México", "Buenos Aires"]
}

df = pd.DataFrame(data)

# Guardar en un archivo Excel
df.to_excel("datos_guardados.xlsx", index=False)

print("Archivo Excel guardado con éxito.")
