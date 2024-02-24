#Practice 1. Regular expressions
#Alumno: Rosiles Hidalgo Emanuel.
#Grupo: 7CM3
import re
from collections import Counter

# Se abre el archivo 'tweets 1.txt' en modo lectura
with open('tweets 1.txt', 'r', encoding='utf-8') as archivo:

    texto = archivo.read() #Representa al texto del archivo de entrada

#------Descripción------
"""Para encontrar cada uno de los 5 strings solicitados se realizaron 5 funciones (una para cada uno) que
reciben como entrada el archivo de texto 'tweets 1.txt'.
En las funciones se definió la expresión regular a utilizar como un patrón mediante la función compile()
y después se aplicó con la función findall(), ambas de la biblioteca 're'. Finalmente se hizo el conteo de
frecuencias con ayuda de la función Counter de la biblioteca 'collections'"""
#-----------------------

#Función para encontrar hashtags
def hashtags(texto):
    print("----------HASHTAGS----------")
    hashtag = re.compile("#\w+")
    resultado = hashtag.findall(texto)
    cont = Counter(resultado)
    frecuencia = cont.most_common(10)
    print(f'Total: {len(resultado)}')
    print('\nTOP 10')
    for hashtg, count in frecuencia:
        print(f"{hashtg} ({count})")
    #print(resultado)

hashtags(texto)

#Función para encontrar nombres de usuario
def users(texto):
    print("----------USERS----------")
    nombre = re.compile("@\w\w+")
    resultado = nombre.findall(texto)
    cont = Counter(resultado)
    frecuencia = cont.most_common(10)
    print(f'Total: {len(resultado)}')
    print('\nTOP 10')
    for usuario, count in frecuencia:
        print(f"{usuario} ({count})")
    #print(resultado)

users(texto)

#Función para encontrar tiempo
def time(texto):
    print("----------TIME----------")
    tiempo = re.compile("\d\d?:\d{2}\s?[ap]?m(?![a-zA-z])|\d\d?\s?[ap][m](?![a-zA-z])|\d\d?:\d{2}|\d\d?\s?[Hh][Rr][Ss]")
    resultado = tiempo.findall(texto)
    cont = Counter(resultado)
    frecuencia = cont.most_common(10)
    print(f'Total: {len(resultado)}')
    print('\nTOP 10')
    for horas, count in frecuencia:
        print(f"{horas} ({count})")
    #print(resultado)

time(texto)

#Función para encontrar emoticones
def emoticons(texto):
    print("----------EMOTICONS----------")
    emoticon = re.compile(":'?-?[/\)(bBdcCDoOpPvV]|(?<!\d):3(?![:\d])|<3")
    resultado = emoticon.findall(texto)
    cont = Counter(resultado)
    frecuencia = cont.most_common(10)
    print(f'Total: {len(resultado)}')
    print('\nTOP 10:')
    for emoticones, count in frecuencia:
        print(f"{emoticones} ({count})")
    #print(resultado)

emoticons(texto)

#Función para encontrar emojis
def emojis(texto):
    print("----------EMOJIS----------")
    emoji = re.compile('[\u263a-\U0001f645]')
    resultado = emoji.findall(texto)
    cont = Counter(resultado)
    frecuencia = cont.most_common(10)
    print(f'Total: {len(resultado)}')
    print('\nTOP 10:')
    for emo, count in frecuencia:
        print(f"{emo} ({count})")
    #print(resultado)

emojis(texto)