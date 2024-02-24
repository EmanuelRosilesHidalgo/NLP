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
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def lematizacion(text):
    doc = nlp(text)
    processed_text = ' '.join([token.lemma_ for token in doc])
    return processed_text

nlp = spacy.load("es_core_news_sm")

# Proceso de tokenizacion y lematizacion  -----------------------------------------------------------------

df = pd.read_excel("Rest_Mex_2022.xlsx")

print(df)

df['Title_Opinion'] = df.apply(lambda row: f"{row['Title']} {row['Opinion']}", axis=1)
df = df.drop(['Title', 'Opinion'], axis=1)

df['Title_Opinion'] = df['Title_Opinion'].apply(lematizacion)

df.to_pickle('df_tokenizacion_lematizacion_final.pkl')
