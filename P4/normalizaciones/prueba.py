import numpy as np
from sklearn.datasets import fetch_20newsgroups
import gensim
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


# Cargar los datos
with open('train_df_lematizado_stopwords.pkl', 'rb') as archivo:
    df_train = pickle.load(archivo)

with open('test_df_lematizado_stopwords.pkl', 'rb') as archivo2:
    df_test = pickle.load(archivo2)

X_train = df_train.data
y_train = df_train.target
X_test = df_test.data
y_test = df_test.target







"""

steps = [
    ('classifier', LogisticRegression())
]

pipe = Pipeline(steps)

# Entrenar el pipeline con los embeddings de entrenamiento
pipe.fit(X_train_embeddings, y_train)

# Realizar predicciones en los embeddings de prueba
y_pred = pipe.predict(X_test_embeddings)

# Evaluar el rendimiento del clasificador
print(classification_report(y_test, y_pred))

"""
steps = [
    ('text_representation', TfidfVectorizer()),
    #('dimensionality_reduction', TruncatedSVD(n_components=2000)),
    ('classifier', MLPClassifier(hidden_layer_sizes=(50, 100), max_iter=400))
    
]
"""steps = [
    ('text_representation', CountVectorizer()),
    # ('dimensionality_reduction', TruncatedSVD(n_components=1000)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=25))  # Utilizar Random Forest
]"""

"""steps = [
    ('text_representation', TfidfVectorizer()),
    # ('dimensionality_reduction', TruncatedSVD(n_components=1000)),
    ('classifier', SVC(kernel='linear'))  # Utilizar Random Forest
]"""

"""steps = [
    ('text_representation', TfidfVectorizer()),
    ('classifier', MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=200)) 
]
"""

pipe = Pipeline(steps)

print (pipe)
pipe.fit(X_train, y_train)

print(len(X_train))
y_pred = pipe.predict(X_test)
print (classification_report(y_test, y_pred))