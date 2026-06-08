# historial_tuplas.py
print("--- HISTORIAL COMBINADO DE LISTAS Y TUPLAS ---")

compra1 = ("Rodrigo", 3, "2026-06-03")
compra2 = ("Juan", 1, "2026-06-03")

# Guardamos las tuplas dentro de una lista mutable
historial = [compra1, compra2]

print("Generando reporte de ventas:")
for factura in historial:
    print(f"- El cliente {factura[0]} compró {factura[1]} unidades en la fecha {factura[2]}.")