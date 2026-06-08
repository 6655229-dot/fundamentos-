# tuplas_inmutables.py
print("--- MANEJO DE TUPLAS INMUTABLES ---")

# Creamos un registro fijo de una venta (Cliente, Cantidad, Fecha)
registro_fijo = ("Rodrigo", 5, "2026-06-03")

print(f"Contenido de la tupla: {registro_fijo}")
print(f"Índice 0 (Nombre): {registro_fijo[0]}")
print(f"Índice 2 (Fecha): {registro_fijo[2]}")

# Código de prueba de inmutabilidad:
# Si intentas descomentar la línea de abajo causará un error (TypeError)
# registro_fijo[0] = "Juan" 
print("\n[INFO] Las tuplas son seguras porque no se pueden modificar por error.")