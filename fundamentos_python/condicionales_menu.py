# condicionales_menu.py
print("--- SISTEMA DE GESTIÓN - TIENDA DE MASCOTAS ---")
nombre = input("Escribe tu nombre de usuario: ")
print(f"Hola {nombre}, inicializando el sistema...\n")

print("¿Qué acción deseas realizar hoy?")
print("1. Consultar inventario total")
print("2. Registrar una compra")
print("3. Salir del sistema")

opcion = int(input("Selecciona una opción (1-3): "))

if opcion == 1:
    print("\n[INFO] El inventario actual de la tienda es de 10 animales.")
elif opcion == 2:
    print("\n[INFO] Has seleccionado: Registrar una compra. (Ver siguiente video).")
elif opcion == 3:
    print(f"\n¡Gracias por usar el sistema, {nombre}! Feliz día.")
else:
    print("\n[ERROR] Opción inválida. Por favor, selecciona 1, 2 o 3.")