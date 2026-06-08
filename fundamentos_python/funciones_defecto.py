# funciones_defecto.py
print("--- FUNCIONES CON PARÁMETROS POR DEFECTO ---")

# Definimos la función. Si no se envía el precio, por defecto será 0.0
def registrar_producto(nombre, cantidad, precio_unitario=0.0):
    total = cantidad * precio_unitario
    print(f"Producto: {nombre} | Cantidad: {cantidad} | Precio: ${precio_unitario}")
    print(f"Total Neto: ${total}\n")

print("1. Llamada enviando todos los datos:")
registrar_producto("Croquetas Perro", 2, 12.50)

print("2. Llamada omitiendo el precio (Usa valor por defecto):")
registrar_producto("Muestra de Juguete", 3)