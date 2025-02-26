from pathlib import Path
import shutil

CARPETA_ORIGEN = Path(input("Seleccione el directorio: ")).expanduser()

CATEGORIAS = {
    "Documentos en PDF": [".pdf"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Música": [".mp3", ".wav"],
    "Archivos ZIP": [".zip", ".rar" ],
    "Python": [".py"],
    "Ejecutables": [".exe", ".msi", ".bat", ".sh"],
    "Documentos": [".doc", ".docx", ".txt"],
    "Otro": []

}

def clasificarArchivos():
    if not CARPETA_ORIGEN.exists():
        print(f"La carpeta '{CARPETA_ORIGEN}' no existe.")
        return
    
    archivosMovidos = {categoria: 0 for categoria in CATEGORIAS}
    archivosMovidos["Otros"] = 0
    
    for archivo in  CARPETA_ORIGEN.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()

            categoriaDestino = "Otros"
            for categoria, extensiones in CATEGORIAS.items():
                if extension in extensiones:
                    categoriaDestino = categoria
                    break

            carpetaDestino = CARPETA_ORIGEN / categoria
            carpetaDestino.mkdir(exist_ok=True)
            archivo.rename(carpetaDestino / archivo.name)
            archivosMovidos[categoriaDestino] += 1

    for categoria, cantidad in archivosMovidos.items():
        if cantidad > 0:
            print(f"{cantidad} archivo(s) movido(s) a la carpeta {categoria}/")

if __name__ == "__main__":
    clasificarArchivos()

