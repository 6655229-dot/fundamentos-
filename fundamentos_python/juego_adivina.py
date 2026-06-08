# juego_adivina.py
import random

def obtener_dado():
    return random.randint(1, 6)

def verificar_intento(usuario, oculto):
    if usuario == oculto:
        return "¡Felicidades! Le pegaste al número correcto."
    else:
        return f"Fallaste. El dado real era {oculto}. Inténtalo de nuevo."

print("=== BIENVENIDO AL JUEGO DEL DADO ===")
dado_real = obtener_dado()

intento = int(input("Adivina el número del dado (1 al 6): "))

# Imprimimos el veredicto de la función
veredicto = verificar_intento(intento, dado_real)
print(veredicto)