"""
Alumno: Rosiles Hidalgo Emanuel.
Grupo: 7CM3.
Práctica 4: Text Classification.
Fecha: 30/10/2023
"""

import numpy as np
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.decomposition import TruncatedSVD
import spacy
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC


#Separación en entrenamiento y prueba
newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')
X_train = newsgroups_train.data
y_train = newsgroups_train.target
X_test = newsgroups_test.data
y_test = newsgroups_test.target

# Crear dataframes para los datos de entrenamiento
train_df = pd.DataFrame({'data': newsgroups_train.data, 'target': newsgroups_train.target})

# Crear dataframes para los datos de prueba
test_df = pd.DataFrame({'data': newsgroups_test.data, 'target': newsgroups_test.target})

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Función para tokenizar
def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return ' '.join(tokens)

# Función para lematizar
def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_tokens = [lemma for lemma in doc]
    return ' '.join(lemmatized_tokens)

# Función para text cleaning (eliminar signos de puntuación)
def eliminar_signos(text):
    doc = nlp(text)
    lemmatized_tokens = [word.text for word in doc if not word.is_punct]
    return ' '.join(lemmatized_tokens)

# Función para eliminar stop words
def eliminar_stop_words(text):
    doc = nlp(text)
    tokens = [word.text for word in doc if not word.is_stop]
    return ' '.join(tokens)


# Ejemplo de abrir el archivo para normalizar
with open('train_df_lematizado.pkl', 'rb') as archivo:
    # Carga los datos desde el archivo .pickle
    df_train_puntos = pickle.load(archivo)

df_train_puntos['data'] = df_train_puntos['data'].apply(eliminar_stop_words) # Aplicar función de normalización

# Guardar el archivo normalizado
with open('train_df_lematizado_stopwords.pkl', 'wb') as file:
    pickle.dump(df_train_puntos, file)


with open('test_df_lematizado.pkl', 'rb') as archivo:
    # Carga los datos desde el archivo .pickle
    df_test_puntos = pickle.load(archivo)

df_test_puntos['data'] = df_test_puntos['data'].apply(eliminar_stop_words) # Aplicar función de normalización

# Guardar el archivo normalizado
with open('test_df_lematizado_stopwords.pkl', 'wb') as file:
    pickle.dump(df_test_puntos, file)

# Cargar los datos
with open('train_df_lematizado_stopwords.pkl', 'rb') as archivo:
    df_train = pickle.load(archivo)

with open('test_df_lematizado_stopwords.pkl', 'rb') as archivo2:
    df_test = pickle.load(archivo2)

X_train = df_train.data
y_train = df_train.target
X_test = df_test.data
y_test = df_test.target

# Representaciones de texto:
"""
TfidfVectorizer() #TF-IDF
CountVectorizer(binary=True) #Binarizada
CountVectorizer() #Frecuencia
TruncatedSVD(n_components=1000) # Reducción de dimensionalidad
TruncatedSVD(n_components=300)
"""

# Clasificadores:
"""
MultinomialNB() #Naive Bayes
LogisticRegression() #Regresión logistica
RandomForestClassifier(n_estimators=100, random_state=25) #Random Forest
SVC(kernel='linear') #Máquina de soporte vectorial
MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=100) #Perceptrón multicapa
MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=200)
MLPClassifier(hidden_layer_sizes=(50, 100), max_iter=400)
"""

#Ejemplo de definición de pasos para Pipeline
steps = [
    ('text_representation', TfidfVectorizer()),
    ('dimensionality_reduction', TruncatedSVD(n_components=1000)),
    ('classifier', SVC(kernel='linear'))  
]

# Aplicar el Pipeline con los pasos definidos a los conjuntos de prueba y entrenamiento
pipe = Pipeline(steps)
print (pipe)
pipe.fit(X_train, y_train)
print(len(X_train))
y_pred = pipe.predict(X_test)
print (classification_report(y_test, y_pred))
