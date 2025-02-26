from pathlib import Path
import shutil

CARPETA_ORIGEN = Path("Descargas")

CATEGORIAS = {
    "Documentos en PDF": [".pdf"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Música": [".mp3", ".wav"],
    "Archivos ZIP": [".zip", ".rar" ],
    "Python": [".py"]
}

def clasificarArchivos():
    if not CARPETA_ORIGEN.exists():
        print(f"La carpeta '{CARPETA_ORIGEN}' no existe.")
        return
    
    for archivo in  CARPETA_ORIGEN.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()

            for categoria, extensiones in CATEGORIAS.items():
                if extension in extensiones:
                    carpetaDestino = CARPETA_ORIGEN / categoria
                    carpetaDestino.mkdir(exist_ok=True)
                    archivo.rename(carpetaDestino / archivo.name)
                    print(f"Movido: {archivo.name} -> {categoria}")
                    break

if __name__ == "__main__":
    clasificarArchivos()

