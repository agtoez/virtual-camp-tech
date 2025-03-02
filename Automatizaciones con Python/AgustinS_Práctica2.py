import pandas as pd

def filtrarVentas(inputFile, outputFile):
    df = pd.read_excel(inputFile, engine='openpyxl')

    dfFiltrado = df[df['Precio'] > 100]

    dfFiltrado.to_excel(outputFile, index=False, engine='openpyxl')
    print(f"Archivo filtrado guardado como: {outputFile}")

archivoEntrada = "ventas.xlsx"
archivoSalida = "ventasFiltradas.xlsx"

filtrarVentas(archivoEntrada, archivoSalida)