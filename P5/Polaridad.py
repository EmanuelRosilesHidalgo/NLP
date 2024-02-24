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
from sklearn.feature_extraction.text import CountVectorizer

def getSELFeatures(cadenas, lexicon_sel, lexicon_emoji):
    features = []
    for cadena in cadenas:
        valor_alegria = 0.0
        valor_enojo = 0.0
        valor_miedo = 0.0
        valor_repulsion = 0.0
        valor_sorpresa = 0.0
        valor_tristeza = 0.0
        valor_positivo = 0.0
        valor_negativo = 0.0
        cadena_palabras = re.split('\s+', cadena)
        dic = {}
        for palabra in cadena_palabras:
            if palabra in lexicon_sel:
                caracteristicas = lexicon_sel[palabra]
                for emocion, valor in caracteristicas:
                    if emocion == 'Alegría':
                        valor_alegria += float(valor)
                    elif emocion == 'Tristeza':
                        valor_tristeza += float(valor)
                    elif emocion == 'Enojo':
                        valor_enojo += float(valor)
                    elif emocion == 'Repulsión':
                        valor_repulsion += float(valor)
                    elif emocion == 'Miedo':
                        valor_miedo += float(valor)
                    elif emocion == 'Sorpresa':
                        valor_sorpresa += float(valor)

            if palabra in lexicon_emoji:
                caracteristicas2 = lexicon_emoji[palabra]
                for polaridad, valor in caracteristicas2:
                    if polaridad == 'positive':
                        valor_positivo = valor_positivo + float(valor)
                    elif polaridad == 'negative':
                        valor_negativo = valor_negativo + float(valor)

        dic['_positive_'] = valor_positivo
        dic['_negative_'] = valor_negativo
        dic['_alegria_'] = valor_alegria
        dic['_tristeza_'] = valor_tristeza
        dic['_enojo_'] = valor_enojo
        dic['_repulsion_'] = valor_repulsion
        dic['_miedo_'] = valor_miedo
        dic['_sorpresa_'] = valor_sorpresa

        dic['acumuladopositivo'] = dic['_alegria_'] + dic['_sorpresa_'] + dic['_positive_']
        dic['acumuladonegative'] = dic['_enojo_'] + dic['_miedo_'] + dic['_repulsion_'] + dic['_tristeza_'] + dic['_negative_']

        features.append(dic)

    return features

def process_text(text):
    doc = nlp(text)
    processed_text = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return processed_text

def process_row(row, lexicon_sel, lexicon_emoji):
    polaridad = getSELFeatures([row['Title_Opinion']], lexicon_sel, lexicon_emoji)
    return polaridad[0] if polaridad else None

nlp = spacy.load("es_core_news_sm")

df = pd.read_pickle("df_tokenizacion_lematizacion_final.pkl")

print(df.iloc[6,:])
with open('lexicon_emoji.pkl', 'rb') as archivo_pickle:
    lexicon_emoji = pickle.load(archivo_pickle)

with open('lexicon_sel.pkl', 'rb') as archivo_pickle2:
    lexicon_sel = pickle.load(archivo_pickle2)

emotions = ['_positive_', '_negative_', '_alegria_', '_tristeza_', '_enojo_', '_repulsion_', '_miedo_', '_sorpresa_', 'acumuladopositivo', 'acumuladonegative']

for emotion in emotions:
    df[emotion] = df['Title_Opinion'].apply(lambda x: process_row({'Title_Opinion': x}, lexicon_sel, lexicon_emoji)[emotion] if process_row({'Title_Opinion': x}, lexicon_sel, lexicon_emoji) else None)

df = df.drop(['Attraction'], axis=1)

df.to_pickle('df_tokenizacion_lematizacion_emojis_final.pkl')

print(df)