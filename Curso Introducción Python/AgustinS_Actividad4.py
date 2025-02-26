def mostrarMenu():
    print("\n📙 MENÚ DE CONTACTOS")    
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")    
    print("3. Buscar contacto por nombre")
    print("4. Eliminar contacto")
    print("5. Actualizar contacto")
    print("6. Salir")

def agregarContacto(agenda):
    nombre = input("Ingrese el nombre: ").strip()
    if any(contacto[0].lower() == nombre.lower() for contacto in agenda):
        print("Contacto existente")
        return
    
    telefono = input("Ingrese el teléfono: ").strip()
    email = input("Ingrese el email: ").strip()
    agenda.append((nombre, telefono, email))
    print("Contacto agendado")

def mostrarContacto(agenda):
    if not agenda:
        print("Lista de contactos vacía")
        return
    print("\n📋 Lista de contactos:")
    for i, (nombre, telefono, mail) in enumerate(agenda, start=1):
        print(f"{i}. Nombre: {nombre} | Teléfono: {telefono} | Email: {mail}")

def buscarContacto(agenda):
    nombre = input("Buscar por nombre: ").strip()
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Contacto encontrado: {contacto[0]} | Teléfono: {contacto[1]} | Email: {contacto[2]}")
            return
    print("Contacto no encontrado.")
    
def eliminarContacto(agenda):
    nombre = input("Ingrese el nombre a eliminar: ").strip()
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            agenda.remove(contacto)
            print("Contacto eliminado.")
            return
    print("Contacto no encontrado.")

def actualizarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto a actualizar: ").strip()
    for i, contacto in enumerate(agenda):
        if contacto[0].lower() == nombre.lower():
            print(f"📌 Contacto actual: {contacto[0]} | Teléfono: {contacto[1]} | Email: {contacto[2]}")
            nuevo_telefono = input("Ingrese el nuevo teléfono (dejar vacío para no cambiar): ").strip()
            nuevo_email = input("Ingrese el nuevo email (dejar vacío para no cambiar): ").strip()
            
            telefono = nuevo_telefono if nuevo_telefono else contacto[1]
            email = nuevo_email if nuevo_email else contacto[2]

            agenda[i] = (contacto[0], telefono, email)
            print("Contacto actualizado correctamente.")
            return
    print("Contacto no encontrado.")

def main():
    agenda = []
    opciones = {
        "1": agregarContacto,
        "2": mostrarContacto,
        "3": buscarContacto,
        "4": eliminarContacto,
        "5": actualizarContacto
    }

    while True:
        mostrarMenu()
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "6":
            print("¡Adiós!")
            break
        elif opcion in opciones:
            opciones[opcion](agenda)
        else:
            print("Opción no válida. Intentá de nuevo.")

if __name__ == "__main__":
    main()