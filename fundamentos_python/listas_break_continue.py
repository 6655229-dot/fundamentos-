# listas_break_continue.py
print("--- CONTROL EN ITERACIONES (BREAK Y CONTINUE) ---")

productos = ["manzana", "pan", "leche", "huevos"]

print("Iniciando recorrido de la lista:")
for item in productos:
    if item == "pan":
        print("-> [CONTINUE] Saltando 'pan' porque no hay en stock.")
        continue  # Salta a la siguiente iteración
        
    print(f"Producto disponible: {item}")
    
    if item == "leche":
        print("-> [BREAK] ¡'leche' encontrada! Frenamos el ciclo aquí.")
        break  # Rompe por completo el bucle for