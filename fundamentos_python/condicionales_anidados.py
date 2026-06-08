# condicionales_anidados.py
print("--- MÓDULO DE COMPRAS ANIDADO ---")
confirmar = input("¿Deseas comprar una mascota? (si/no): ").lower()

if confirmar == "si":
    print("\nMascotas disponibles: perro, gato, ave")
    animal = input("¿Qué animal deseas elegir?: ").lower()
    
    # Condicionales anidados (un IF dentro de otro IF)
    if animal == "perro":
        print("-> Has elegido un Perro. El costo es de $50.00")
    elif animal == "gato":
        print("-> Has elegido un Gato. El costo es de $40.00")
    elif animal == "ave":
        print("-> Has elegido un Ave. El costo es de $25.00")
    else:
        print("-> [ERROR] Lo sentimos, esa especie no la manejamos.")
else:
    print("\nCompra cancelada. Regresando al menú principal.")