# diccionarios_inventario.py
print("--- DICCIONARIOS EN PYTHON (LLAVE: VALOR) ---")

# Definimos el diccionario de stock de animales
inventario = {
    "perro": 3,
    "gato": 5,
    "ave": 0
}

print("Estructura completa:", inventario)

print("\nRecorriendo llaves y valores individualmente:")
for llave, valor in inventario.items():
    print(f"Mascota: {llave.capitalize()} | Existencias en tienda: {valor}")