# sistema_tienda_final.py
print("--- SISTEMA INTEGRAL DE CONTROL DE STOCK ---")

inventario = {"perro": 2, "ave": 0}
carrito = []
pedido = "perro"

print(f"Inventario antes de la compra: {inventario}")

# 1. Validar existencia de la clave
if pedido in inventario:
    # 2. Validar stock disponible
    if inventario[pedido] > 0:
        # 3. Validar que no esté duplicado en el carrito
        if pedido not in carrito:
            carrito.append(pedido)
            inventario[pedido] -= 1  # Restamos una unidad del stock
            print(f"¡Éxito! '{pedido}' añadido al carrito de compras.")
    else:
        print(f"Lo sentimos, '{pedido}' está agotado.")
else:
    print("Ese animal no pertenece a la tienda.")

print(f"\nCarrito final: {carrito}")
print(f"Inventario actualizado: {inventario}")