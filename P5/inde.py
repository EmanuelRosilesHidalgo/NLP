
import pickle


with open('lexicon_emoji.pkl', 'rb') as archivo_pickle:
    lexicon = pickle.load(archivo_pickle)

# Obtén las características del índice deseado
c1, c2 = lexicon['😄']

print(c1)


"""with open('lexicon_sel.pkl', 'rb') as archivo_pickle:
    lexicon = pickle.load(archivo_pickle)

c1, c2 = lexicon['hastiar']

print(c2)


import pandas as pd

# Supongamos que tienes un DataFrame df con las columnas 'emoji', 'negative' y 'positive'
# Aquí hay un ejemplo de DataFrame de prueba
data = {'emoji': ['😊', '😢', '👍', '👎'],
        'negative': [-0.5, -0.8, -0.3, -0.7],
        'positive': [0.6, 0.2, 0.8, 0.5]}

df = pd.DataFrame(data)

# Crear un diccionario donde cada emoji tenga asociadas listas de tuplas (polaridad, valor)
diccionario_caracteristicas = {}

for indice, fila in df.iterrows():
    emoji = fila['emoji']
    tupla_negative = ('negative', fila['negative'])
    tupla_positive = ('positive', fila['positive'])
    
    # Si el emoji ya está en el diccionario, actualiza las listas existentes
    if emoji in diccionario_caracteristicas:
        diccionario_caracteristicas[emoji].extend([tupla_negative, tupla_positive])
    else:
        diccionario_caracteristicas[emoji] = [tupla_negative, tupla_positive]

# Muestra el diccionario resultante
a1, a2 = diccionario_caracteristicas['😊']

print(a1)"""