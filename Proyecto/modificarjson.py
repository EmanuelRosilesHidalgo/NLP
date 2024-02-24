import json
import pandas as pd
import re

def limpiar_puntos_espacios(texto):
    # Utilizar expresión regular para eliminar puntos que no están al final de una palabra
    texto_sin_puntos = re.sub(r'(?<!\w)\.(?!\w)', '', texto)
    texto_sin_espacios_extras = re.sub(r'\s+', ' ', texto_sin_puntos)

    return texto_sin_espacios_extras

def eliminar_enlaces(texto):
    # Patrón de expresión regular para encontrar enlaces
    patron_enlace = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    # Utilizar re.sub para reemplazar los enlaces con una cadena vacía
    texto_sin_enlaces = re.sub(patron_enlace, '', texto)
    
    return texto_sin_enlaces

# Ruta al archivo JSON
archivo_json = 'comentarios_profesores_ver1.json'

# Abrir el archivo en modo lectura
with open(archivo_json, 'r') as archivo:
    # Cargar el contenido JSON
    datos_json = json.load(archivo)



for i in range(len(datos_json)):
    texto = '. '.join(datos_json[i]["Comentarios"]) + ". "
    texto2 = eliminar_enlaces(texto)
    datos_json[i]["Comentarios"] = limpiar_puntos_espacios(texto2)

#print(datos_json[0]["Comentarios"])


df = pd.DataFrame(datos_json, columns=["Nombre", "Calificacion", "Comentarios"])


print(df.head())

# Guardar el DataFrame en un archivo .pkl
df.to_pickle('comentarios_df_clean1_final.pkl')
