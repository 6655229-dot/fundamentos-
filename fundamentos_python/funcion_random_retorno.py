# funcion_random_retorno.py
import random

print("--- SISTEMA DE LANZAMIENTO DE DADOS ---")

# Función que genera y devuelve un número aleatorio
def lanzar_dado_aleatorio():
    numero_secreto = random.randint(1, 6)
    return numero_secreto  # Devuelve el valor al programa principal

# Guardamos el resultado devuelto en una variable
resultado = lanzar_dado_aleatorio()
print(f"[SISTEMA] El dado cayó secretamente en el número: {resultado}")