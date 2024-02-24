import spacy
import pandas as pd
import numpy as np
import re 
import argparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def normalizacion_archivo(noticia_prueba):
    with open(noticia_prueba, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            doc = nlp(linea)
            lista_lemmas = []

            for token in doc: 
                lista_lemmas.append(token.lemma_)
            texto_lematizado = " ".join(lista_lemmas)
            doc2 = nlp(texto_lematizado)
            texto_limpio = []

            diccionario_articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas", "Al", "Del"]
            diccionario_preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "sobre", "tras",
                                        "A", "Ante", "Bajo", "Cabe", "Con", "Contra", "De", "Desde", "Durante", "En", "Entre", "Hacia", "Hasta", "Mediante", "Para", "Por", "Según", "Sin", "Sobre", "Tras"]
            diccionario_conjunciones = ["y", "e", "ni", "que", "o", "u", "pero", "aunque", "sin embargo", "porque", "pues", "ya que", "si", "sino", "además", "también", "como", "así que", "de modo que", "entonces", "por lo tanto", "por consiguiente", "a fin de que", "para que", "a pesar de que", "a no ser que", "a menos que", "a condición de que", "en caso de que", "aunque", "a pesar de", "por lo que", "aun cuando", "a partir de que", "en cuanto", "a medida que", "a raíz de que", "a su vez", "a diferencia de", "en cambio", "sin que", "mientras", "a la vez", "por otro lado", "de otra manera", "por el contrario",
                                        "Y", "Ni", "Que", "O", "U", "Pero", "Aunque", "Sin embargo", "Porque", "Pues", "Ya que", "Si", "Sino", "Además", "También", "Como", "Así que", "De modo que", "Entonces", "Por lo tanto", "Por consiguiente", "A fin de que", "Para que", "A pesar de que", "A no ser que", "A menos que", "A condición de que", "En caso de que", "Aunque", "A pesar de", "Por lo que", "Aun cuando", "A partir de que", "En cuanto", "A medida que", "A raíz de que", "A su vez", "A diferencia de", "En cambio", "Sin que", "Mientras", "A la vez", "Por otro lado", "De otra manera", "Por el contrario"]
            diccionario_pronombres = ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "vosotros", "vosotras", "ellos", "ellas", "ustedes", 
                                    "Yo", "Tú", "Él", "Ella", "Nosotros", "Nosotras", "Vosotros", "Vosotras", "Ellos", "Ellas", "Me", "Te", "Lo", "La", "Nos", "Os", "Los", "Las", "Se", "Mi", "Mío", "Mía", "Míos", "Mías", "Tu", "Tuyo", "Tuya", "Tuyos", "Tuyas", "Su", "Suyo", "Suya", "Suyos", "Suyas", "Nuestro", "Nuestra", "Nuestros", "Nuestras", "Vuestro", "Vuestra", "Vuestros", "Vuestras", "Este", "Esta", "Estos", "Estas", "Ese", "Esa", "Esos", "Esas", "Aquel", "Aquella", "Aquellos", "Aquellas", "Alguno", "Alguna", "Algunos", "Algunas", "Ninguno", "Ninguna", "Ningunos", "Ningunas", "Uno", "Una", "Unos", "Unas", "Otro", "Otra", "Otros", "Otras", "Que", "Cual", "Quien", "Quienes", "Suyo", "Suya", "Suyos", "Suyas", "Usted", "Ustedes", "Vos"]

            for lemma in doc2:
                if(lemma.pos_ != "DET" and lemma.pos_ != "ADP" and lemma.pos_ != "CONJ" and lemma.pos_ != "PRON" and lemma.text not in diccionario_articulos 
                and lemma.text not in diccionario_pronombres and lemma.text not in diccionario_preposiciones and lemma.text not in diccionario_conjunciones):
                    texto_limpio.append(lemma.text)

            texto_resultado = " ".join(texto_limpio) 
            texto_sin_espacios = re.sub('\s+', ' ', texto_resultado) 
            texto_final = texto_sin_espacios.strip()

            return texto_final

nlp = spacy.load("es_core_news_sm")

noticias = []

with open('corpus_normalizado.txt', 'r', encoding='utf-8') as archivo:
    corpus = archivo.readlines()

for linea in corpus:
    noticias.append({"Texto": linea})

df = pd.DataFrame(noticias)

""" Mostrar los primeros 5 documentos """
primeros_5_documentos = df.head(5)
# print(primeros_5_documentos)

""" Representacion vectorial binaria """
vectorizer = CountVectorizer(binary=True)
representacion_binaria = vectorizer.fit_transform(df['Texto'])
df_representacion_binaria = pd.DataFrame(representacion_binaria.toarray(), columns=vectorizer.get_feature_names_out())
# print(df_representacion_binaria)

""" Representacion vectorial frecuencia """
count_vectorizer = CountVectorizer()
representacion_frecuencia = count_vectorizer.fit_transform(df['Texto'])
df_representacion_frecuencia = pd.DataFrame(representacion_frecuencia.toarray(), columns=count_vectorizer.get_feature_names_out())
# print(df_representacion_frecuencia)

""" Representacion vectorial Tfidf """
tfidf_vectorizer = TfidfVectorizer()
representacion_tfidf = tfidf_vectorizer.fit_transform(df['Texto'])
df_representacion_tfidf = pd.DataFrame(representacion_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
# print(df_representacion_tfidf)

# Tratamiento de la noticia de prueba

""" Normalizacion y vectorizacion de la nueva noticia"""
noticia_normalizada = normalizacion_archivo('prueba01.txt')

opcion_elegida = 'frecuencia'

if opcion_elegida == "binaria":
    print("Opción elegida: binaria")
    representacion_vectorial_nueva_noticia = vectorizer.transform([noticia_normalizada])
    df_representacion_binaria_nueva_noticia = pd.DataFrame(representacion_vectorial_nueva_noticia.toarray(), columns=vectorizer.get_feature_names_out())
    similitud_coseno = cosine_similarity(representacion_vectorial_nueva_noticia, representacion_binaria)
    
elif opcion_elegida == "frecuencia":
    print("Opción elegida: frecuencia")
    representacion_vectorial_nueva_noticia = count_vectorizer.transform([noticia_normalizada])
    df_representacion_frecuencia_nueva_noticia = pd.DataFrame(representacion_vectorial_nueva_noticia.toarray(), columns=count_vectorizer.get_feature_names_out())
    similitud_coseno = cosine_similarity(representacion_vectorial_nueva_noticia, representacion_frecuencia)
    
elif opcion_elegida == "tfidf":
    print("Opción elegida: tfidf")
    representacion_vectorial_nueva_noticia = tfidf_vectorizer.transform([noticia_normalizada])
    df_representacion_frecuencia_nueva_noticia = pd.DataFrame(representacion_vectorial_nueva_noticia.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    similitud_coseno = cosine_similarity(representacion_vectorial_nueva_noticia, representacion_tfidf)

# Pasar del arreglo con un solo elemento a una lista de todas las similitudes
arreglo_similitud = np.array(similitud_coseno)
lista_similitud = arreglo_similitud.flatten().tolist()

# Dataframe para poder ordenar las similitudes
numeros_documentos = []
for i in range(len(lista_similitud)):
    numero_documento = "Documento " + str(i + 1)
    numeros_documentos.append(numero_documento)

df_similitud = pd.DataFrame({"Documento": numeros_documentos, "Similitud": lista_similitud})
df_similitud = df_similitud.sort_values(by="Similitud", ascending=False)
print(df_similitud)