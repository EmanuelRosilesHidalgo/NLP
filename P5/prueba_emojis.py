import os.path
import sys
import pickle
import re
import numpy as np
import spacy
import pandas as pd
from scipy.sparse import hstack
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
 
def load_sel():
    #~ global lexicon_sel
    lexicon_sel = {}
    input_file = open('SEL_full.txt', 'r')
    for line in input_file:
        #Las líneas del lexicon tienen el siguiente formato:
        #abundancia 0   0   50  50  0.83    Alegría
        
        palabras = line.split("\t")
        palabras[6]= re.sub('\n', '', palabras[6])
        pair = (palabras[6], palabras[5])
        if lexicon_sel:
            if palabras[0] not in lexicon_sel:
                lista = [pair]
                lexicon_sel[palabras[0]] = lista
            else:
                lexicon_sel[palabras[0]].append (pair)
        else:
            lista = [pair]
            lexicon_sel[palabras[0]] = lista
    input_file.close()
    del lexicon_sel['Palabra']; #Esta llave se inserta porque es parte del encabezado del diccionario, por lo que se requiere eliminar
    #Estructura resultante
        #'hastiar': [('Enojo\n', '0.629'), ('Repulsion\n', '0.596')]
    return lexicon_sel


def load_sel():
    #~ global lexicon_sel
    lexicon_sel = {}
    input_file = open('SEL_full.txt', 'r')
    for line in input_file:
        #Las líneas del lexicon tienen el siguiente formato:
        #abundancia 0   0   50  50  0.83    Alegría
        
        palabras = line.split("\t")
        palabras[1]= re.sub('\n', '', palabras[6])
        pair = (palabras[6], palabras[5])
        if lexicon_sel:
            if palabras[0] not in lexicon_sel:
                lista = [pair]
                lexicon_sel[palabras[0]] = lista
            else:
                lexicon_sel[palabras[0]].append (pair)
        else:
            lista = [pair]
            lexicon_sel[palabras[0]] = lista
    input_file.close()
    del lexicon_sel['Palabra']; #Esta llave se inserta porque es parte del encabezado del diccionario, por lo que se requiere eliminar
    #Estructura resultante
        #'hastiar': [('Enojo\n', '0.629'), ('Repulsion\n', '0.596')]
    return lexicon_sel


def getSELFeatures(cadenas, lexicon_sel, lexicon_emojis):
    #'hastiar': [('Enojo\n', '0.629'), ('Repulsi\xf3n\n', '0.596')]
    features = []
    for cadena in cadenas:
        valor_alegria = 0.0
        valor_enojo = 0.0
        valor_miedo = 0.0
        valor_repulsion = 0.0
        valor_sorpresa = 0.0
        valor_tristeza = 0.0
        cadena_palabras = re.split('\s+', cadena)
        dic = {}
        for palabra in cadena_palabras:
            if palabra in lexicon_sel:
                caracteristicas = lexicon_sel[palabra]
                for emocion, valor in caracteristicas:
                    if emocion == 'Alegría':
                        valor_alegria = valor_alegria + float(valor)
                    elif emocion == 'Tristeza':
                        valor_tristeza = valor_tristeza + float(valor)
                    elif emocion == 'Enojo':
                        valor_enojo = valor_enojo + float(valor)
                    elif emocion == 'Repulsión':
                        valor_repulsion = valor_repulsion + float(valor)
                    elif emocion == 'Miedo':
                        valor_miedo = valor_miedo + float(valor)
                    elif emocion == 'Sorpresa':
                        valor_sorpresa = valor_sorpresa + float(valor)
        dic['__alegria__'] = valor_alegria
        dic['__tristeza__'] = valor_tristeza
        dic['__enojo__'] = valor_enojo
        dic['__repulsion__'] = valor_repulsion
        dic['__miedo__'] = valor_miedo
        dic['__sorpresa__'] = valor_sorpresa



        #Esto es para los valores acumulados del mapeo a positivo (alegría + sorpresa) y negativo (enojo + miedo + repulsión + tristeza)
        dic['acumuladopositivo'] = dic['__alegria__'] + dic['__sorpresa__']
        dic['acumuladonegative'] = dic['__enojo__'] + dic['__miedo__'] + dic['__repulsion__'] + dic['__tristeza__']
        
        features.append (dic)
    
    return features

print(getSELFeatures())
