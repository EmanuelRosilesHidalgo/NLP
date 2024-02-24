import pickle
import pandas as pd

# Especifica el nombre del archivo de texto
nombre_archivo = 'emojis.txt'

# Lee el archivo de texto y crea un DataFrame
dataframe = pd.read_csv(nombre_archivo, sep='\t', header=None)  # Ajusta el delimitador según el formato de tu archivo


df_recortado = dataframe.iloc[:, [2, 11, 12]]

print(df_recortado)

df_recortado.to_csv("lexicon_emojis.txt", sep='\t', index=False)  # Ajusta el delimitador según tus necesidades

print(f"DataFrame exportado como lexicon_emojis.txt")


# Supongamos que tienes un DataFrame llamado df con las columnas 'emoji', 'negative' y 'positive'
# Aquí tienes un ejemplo de DataFrame de prueba

# Lee el archivo CSV especificando los nombres de las columnas
df = pd.read_csv('lexicon_emojis.txt', sep='\t', header=None, names=['emoji', 'negative', 'positive'])

# Elimina los duplicados basados en la columna 'emoji'
df_sin_duplicados = df.drop_duplicates('emoji')


# Crear un diccionario donde cada emoji tenga asociadas listas de tuplas (polaridad, valor)
diccionario_caracteristicas = {}

for indice, fila in df_sin_duplicados.iterrows():
    emoji = fila['emoji']
    tupla_negative = ('negative', fila['negative'])
    tupla_positive = ('positive', fila['positive'])
    
    # Si el emoji ya está en el diccionario, actualiza las listas existentes
    if emoji in diccionario_caracteristicas:
        diccionario_caracteristicas[emoji].extend([tupla_negative, tupla_positive])
    else:
        diccionario_caracteristicas[emoji] = [tupla_negative, tupla_positive]
        
# Muestra el diccionario resultante
nombre_archivo_pickle = 'lexicon_emoji.pkl'

# Guarda el diccionario en el archivo pickle
with open(nombre_archivo_pickle, 'wb') as archivo_pickle:
    pickle.dump(diccionario_caracteristicas, archivo_pickle)
