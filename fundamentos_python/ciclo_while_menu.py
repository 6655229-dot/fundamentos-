# ciclo_while_menu.py
print("--- DEMOSTRACIÓN DE BUCLE WHILE ---")

ejecutando = True

while ejecutando:
    print("\n*** MENÚ ACTIVO ***")
    print("1. Mostrar saludo")
    print("2. Salir del bucle")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("\n¡Hola! El ciclo while sigue repitiéndose porque la condición es True.")
    elif opcion == "2":
        print("\n[PROCESO] Cambiando la variable a False para romper el ciclo...")
        ejecutando = False  # Aquí se detiene el While
    else:
        print("\nOpción no válida. Intenta de nuevo.")

print("El ciclo ha terminado con éxito.")