import re

def limpiar_puntos_espacios(texto):
    # Utilizar expresión regular para eliminar puntos que no están al final de una palabra
    texto_sin_puntos = re.sub(r'(?<!\w)\.(?!\w)', '', texto)
    texto_sin_espacios_extras = re.sub(r'\s+', ' ', texto_sin_puntos)

    return texto_sin_espacios_extras

def eliminar_espacios_extras(texto):
    # Utilizar expresión regular para reemplazar espacios múltiples con uno solo
    texto_sin_espacios_extras = re.sub(r'\s+', ' ', texto)

    return texto_sin_espacios_extras.strip()  # Eliminar espacios al principio y al final, si es necesario



# Ejemplo de uso
texto_original = "Este es un ejemplo....... . con puntos. Algunos.     punt    os intermedios."
texto_resultado = limpiar_puntos_espacios(texto_original)

print("Texto original:", texto_original)
print("Texto resultado:", texto_resultado)

