def menu():
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
        print("❌Contacto existente")
        return
    
    telefono = input("Ingrese el teléfono: ").strip()
    email = input("Ingrese el email: ").strip()
    agenda.append((nombre, telefono, email))
    print("✅Contacto agendado")

def mostrarContacto(agenda):
    if not agenda:
        print("Lista de contactos vacía")
        return
    print("\n📋 Lista de contactos:")
    for i, (nombre, telefono, mail) in enumerate(agenda, start=1):
        print(f"{i}. Nombre: {nombre} | Teléfono: {telefono} | Email: {mail}")

def buscarContacto(agenda):
    pass
def eliminarContacto(agenda):
    pass
def actualizarContacto(agenda):
    pass
def main():
    pass

menu()