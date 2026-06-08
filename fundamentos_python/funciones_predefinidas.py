# funciones_predefinidas.py
print("--- PRUEBA DE FUNCIONES PREDEFINIDAS ---")

# Texto original simulando un error común de usuario con espacios de más
texto_usuario = "   rodrigo alvarado   "

print(f"Texto original: '{texto_usuario}'")

# Aplicando .strip() para limpiar espacios en los extremos
texto_limpio = texto_usuario.strip()
print(f"Con strip(): '{texto_limpio}'")

# Aplicando .upper() para convertir a mayúsculas
texto_mayusculas = texto_limpio.upper()
print(f"Con upper(): '{texto_mayusculas}'")