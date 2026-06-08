# listas_mutables.py
print("--- MANEJO DE LISTAS MUTABLES ---")

# Inicializamos una lista con elementos de compra
carrito = ["manzana", "pan"]
print(f"Lista inicial: {carrito}")

# Añadiendo elementos dinámicamente
carrito.append("leche")
carrito.append("huevos")

print(f"Lista final modificada con append(): {carrito}")
print(f"Total de productos en el carrito: {len(carrito)}")