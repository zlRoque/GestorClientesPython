import os
from datetime import datetime

# Carpeta donde se guardarán los archivos de clientes
CARPETA_CLIENTES = "clientes"

# Crear la carpeta si no existe
if not os.path.exists(CARPETA_CLIENTES):
    os.makedirs(CARPETA_CLIENTES)

# ========================= FUNCIONES =========================

def crear_cliente():
    print("🧾 Crear nuevo cliente")
    nombre = input("Ingrese el nombre del cliente (ejemplo: ana_garcia): ").strip()
    archivo = os.path.join(CARPETA_CLIENTES, f"{nombre}.txt")
    
    if os.path.exists(archivo):
        print("⚠️ El cliente ya existe.")
        return
    
    telefono = input("Ingrese el teléfono del cliente: ").strip()
    correo = input("Ingrese el correo del cliente: ").strip()
    primera_solicitud = input("Ingrese la descripción de la primera solicitud: ").strip()
    
    fecha_registro = datetime.now().strftime("%Y-%m-%d")
    id_cliente = nombre[:2].upper() + datetime.now().strftime("%Y%m%d%H%M%S")
    
    with open(archivo, "w") as f:
        f.write(f"Nombre: {nombre}\n")
        f.write(f"ID_Cliente: {id_cliente}\n")
        f.write(f"Telefono: {telefono}\n")
        f.write(f"Correo: {correo}\n")
        f.write(f"FechaRegistro: {fecha_registro}\n")
        f.write("Servicios:\n")
        f.write(f"- {primera_solicitud} ({fecha_registro})\n")
    
    print("✅ Cliente creado correctamente.")

def listar_clientes():
    print("📋 Lista de clientes:")
    archivos = [f.replace(".txt","") for f in os.listdir(CARPETA_CLIENTES) if f.endswith(".txt")]
    if archivos:
        for cliente in archivos:
            print(f"- {cliente}")
    else:
        print("No hay clientes registrados.")

def ver_cliente():
    nombre = input("Ingrese el nombre del cliente a consultar: ").strip()
    archivo = os.path.join(CARPETA_CLIENTES, f"{nombre}.txt")
    
    if not os.path.exists(archivo):
        print("❌ Cliente no encontrado.")
        return
    
    print("------ Información del cliente ------")
    with open(archivo, "r") as f:
        print(f.read())
    print("------------------------------------")

def modificar_cliente():
    listar_clientes()
    nombre = input("Ingrese el nombre del cliente a modificar: ").strip()
    archivo = os.path.join(CARPETA_CLIENTES, f"{nombre}.txt")
    
    if not os.path.exists(archivo):
        print("❌ Cliente no encontrado.")
        return
    
    nueva_solicitud = input("Ingrese la nueva solicitud o servicio: ").strip()
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    with open(archivo, "a") as f:
        f.write(f"- {nueva_solicitud} ({fecha})\n")
    
    print("✅ Solicitud agregada correctamente.")

def eliminar_cliente():
    listar_clientes()
    nombre = input("Ingrese el nombre del cliente a eliminar: ").strip()
    archivo = os.path.join(CARPETA_CLIENTES, f"{nombre}.txt")
    
    if not os.path.exists(archivo):
        print("❌ Cliente no encontrado.")
        return
    
    confirmar = input("¿Está seguro de eliminar este cliente? (s/n): ").lower()
    if confirmar == "s":
        os.remove(archivo)
        print("✅ Cliente eliminado correctamente.")
    else:
        print("❌ Operación cancelada.")

# ========================= MENÚ PRINCIPAL =========================

def menu():
    while True:
        print("\n========= MENÚ AXANET =========")
        print("1. Crear nuevo cliente")
        print("2. Listar clientes")
        print("3. Ver cliente")
        print("4. Modificar cliente")
        print("5. Eliminar cliente")
        print("6. Salir")
        print("===============================")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            ver_cliente()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❗ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
