from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.decomposition import TruncatedSVD
import spacy
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


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

def normalize_text(text):
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(lemmatized_tokens)


def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return ' '.join(tokens)

def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_tokens = [lemma for lemma in doc]
    return ' '.join(lemmatized_tokens)

def eliminar_signos(text):
    doc = nlp(text)
    lemmatized_tokens = [word.text for word in doc if not word.is_punct]
    return ' '.join(lemmatized_tokens)

def eliminar_stop_words(text):
    doc = nlp(text)
    tokens = [word.text for word in doc if not word.is_stop]
    return ' '.join(tokens)


"""def normalize_text(text):
    doc = nlp(text)
    tokenized_documents = []

    for i in len(text):
        texto = 
        tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        tokenized_document = ' '.join(tokens)
        
        # Agregar el documento tokenizado a la lista
        tokenized_documents.append(tokenized_document)

    return tokenized_document"""

# Aplicar la lematización a los datos de entrenamiento
#train_df['data'] = train_df['data'].apply(eliminar_signos)

# Aplicar la lematización a los datos de prueba
#test_df['data'] = test_df['data'].apply(lemmatize_text)

with open('test_df_lematizado.pkl', 'rb') as archivo:
    # Carga los datos desde el archivo .pickle
    df_train_puntos = pickle.load(archivo)

df_train_puntos['data'] = df_train_puntos['data'].apply(eliminar_stop_words)


# Guardar normalized_X_train
with open('test_df_lematizado_stopwords.pkl', 'wb') as file:
    pickle.dump(df_train_puntos, file)


# Guardar normalized_X_test
"""with open('test_df_lematizado2.pkl', 'wb') as file:
    pickle.dump(test_df, file)"""



"""with open('train_df_lematizado.pkl', 'rb') as archivo:
    # Carga los datos desde el archivo .pickle
    df_train = pickle.load(archivo)


with open('test_df_lematizado.pkl', 'rb') as archivo2:
    # Carga los datos desde el archivo .pickle
    df_test = pickle.load(archivo2)"""


"""with open('test_df_lematizado_puntuacion.pkl', 'rb') as archivo3:
    # Carga los datos desde el archivo .pickle
    df_test_tokenizado = pickle.load(archivo3)

with open('test_df_lematizado_puntuacion.pkl', 'rb') as archivo4:
    # Carga los datos desde el archivo .pickle
    df_test_tokenizado = pickle.load(archivo3)"""

"""print(len(df_train_normalizado.columns))
print(len(df_test_normalizado.columns))"""

"""
print("-----------------------------Original")
print(df_train_tokenizado.iloc[50,0])
print("---------------------------MIO")
print(df_train_tokenizado2.iloc[50,0])"""
"""print("----------------------------LALO")
print(df_train_normalizado2.iloc[0,0]) 
""" 

"""vectorizer = TfidfVectorizer()
vectors_train = vectorizer.fit_transform(df_train.data)
print (vectorizer.get_feature_names_out())
print (len(vectorizer.get_feature_names_out()))

n_components_svd = 300  # Número de componentes SVD deseado
svd = TruncatedSVD(n_components_svd)
tfidf_svd = svd.fit_transform(vectors_train)"""

"""X_train = df_train.data
y_train = df_train.target
X_test = df_test.data
y_test = df_test.target


steps = [
    ('text_representation', TfidfVectorizer()),
    ('dimensionality_reduction', TruncatedSVD(n_components=300)),
    ('classifier', MultinomialNB())
]


pipe = Pipeline(steps)

print (pipe)
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
print (classification_report(y_test, y_pred))
"""

"""vectorizer = CountVectorizer(binary=True)
vectors_train = vectorizer.fit_transform(df_train.data)
print (vectorizer.get_feature_names_out())
print (len(vectorizer.get_feature_names_out()))"""


"""vectorizer = CountVectorizer()
vectors_train = vectorizer.fit_transform(df_train.data)
print (vectorizer.get_feature_names_out())
print (len(vectorizer.get_feature_names_out()))
"""


#Clasificadores
"""clf = MultinomialNB()
clf.fit(vectors_train, df_train.target)
vectors_test = vectorizer.transform(df_test.data)
y_pred = clf.predict(vectors_test)
print ('*****************Naïve Bayes****************')
print (y_pred)
# ~ print ('vectors_train.shape {}'.format(vectors_train.shape))
# ~ print ('vectors_test.shape {}'.format(vectors_test.shape))
print (classification_report(df_test.target, y_pred))"""


#MNB SVD
"""clf = MultinomialNB()
clf.fit(tfidf_svd, y_train)
vectors_test = vectorizer.transform(newsgroups_test.data)
tfidf_svd_test = svd.transform(vectors_test)
y_pred = clf.predict(tfidf_svd_test)
print('*****************Naïve Bayes****************')
print(y_pred)
print(classification_report(y_test, y_pred))"""

"""clf = LogisticRegression()
clf.fit(vectors_train, df_train.target)
vectors_test = vectorizer.transform(df_test.data)
y_pred = clf.predict(vectors_test)
print ('*****************Naïve Bayes****************')
print (y_pred)
# ~ print ('vectors_train.shape {}'.format(vectors_train.shape))
# ~ print ('vectors_test.shape {}'.format(vectors_test.shape))
print (classification_report(df_test.target, y_pred))"""

"""clf = LogisticRegression()
clf.fit(X_train, y_train)
vectors_test = vectorizer.transform(y_test)
y_pred = clf.predict(y_test)
print ('*****************Naïve Bayes****************')
print (y_pred)
# ~ print ('vectors_train.shape {}'.format(vectors_train.shape))
# ~ print ('vectors_test.shape {}'.format(vectors_test.shape))
print (classification_report(y_test, y_pred))"""