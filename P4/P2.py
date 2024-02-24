"""
Practice 2. Text normalization.
Alumno: Rosiles Hidalgo Emanuel.
Grupo: 7CM3
"""

import spacy
import re

# Abre el archivo "corpus_noticias.txt" en modo lectura
with open('/Prácticas/nuevo_corpus.txt', 'r', encoding='utf-8') as archivo:
    #Se almacenan las lineas del archivo en una lista
    lineas = archivo.readlines()

# Se crea un nuevo archivo llamado "nuevo_corpus.txt" y se abre en modo escritura
archivo_nuevo = open('/Prácticas/nuevo_corpus.txt', 'w', encoding='utf-8')

#Se carga el modelo de lenguaje en español
nlp = spacy.load("es_core_news_sm")

#Se lee linea por linea el archivo de noticias para no llenar la memoria
for linea in lineas:
    contenido = linea.strip().split('&&&&&&&&') #Se identifican las partes principales de la noticia
    cuerpo_noticia = contenido[2] #Se obtiene el cuerpo de la noticia
    doc = nlp(cuerpo_noticia) #Se procesa el cuerpo de la notica usando el modelo cargado en nlp
    lista_lemmas = [] #Se crea una lista para los lemas identificados

    #Ciclo para tokenizar el cuerpo de la noticia
    for token in doc: 
        lista_lemmas.append(token.lemma_) #Se obtiene el lema de cada token y se almacena en la lista de lemas
    texto_lematizado = " ".join(lista_lemmas) #Al finalizar la tokenización se genera el nuevo texto con los lemas obtenidos de cada token
    doc2 = nlp(texto_lematizado) #Se procesa el texto lematizado con el modelo cargado en nlp
    texto_limpio = [] #Se crea una lista para almacenar las palabras que no sean stop words

    #Diccionarios para complementar la eliminación de las stop words con spacy
    diccionario_articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas", "Al", "Del"]

    diccionario_preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "sobre", "tras",
                                 "A", "Ante", "Bajo", "Cabe", "Con", "Contra", "De", "Desde", "Durante", "En", "Entre", "Hacia", "Hasta", "Mediante", "Para", "Por", "Según", "Sin", "Sobre", "Tras"]

    
    diccionario_conjunciones = ["y", "e", "ni", "que", "o", "u", "pero", "aunque", "sin embargo", "porque", "pues", "ya que", "si", "sino", "además", "también", "como", "así que", "de modo que", "entonces", "por lo tanto", "por consiguiente", "a fin de que", "para que", "a pesar de que", "a no ser que", "a menos que", "a condición de que", "en caso de que", "aunque", "a pesar de", "por lo que", "aun cuando", "a partir de que", "en cuanto", "a medida que", "a raíz de que", "a su vez", "a diferencia de", "en cambio", "sin que", "mientras", "a la vez", "por otro lado", "de otra manera", "por el contrario",
                                "Y", "Ni", "Que", "O", "U", "Pero", "Aunque", "Sin embargo", "Porque", "Pues", "Ya que", "Si", "Sino", "Además", "También", "Como", "Así que", "De modo que", "Entonces", "Por lo tanto", "Por consiguiente", "A fin de que", "Para que", "A pesar de que", "A no ser que", "A menos que", "A condición de que", "En caso de que", "Aunque", "A pesar de", "Por lo que", "Aun cuando", "A partir de que", "En cuanto", "A medida que", "A raíz de que", "A su vez", "A diferencia de", "En cambio", "Sin que", "Mientras", "A la vez", "Por otro lado", "De otra manera", "Por el contrario"]
    
    diccionario_pronombres = ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "vosotros", "vosotras", "ellos", "ellas", "ustedes", 
                              "Yo", "Tú", "Él", "Ella", "Nosotros", "Nosotras", "Vosotros", "Vosotras", "Ellos", "Ellas", "Me", "Te", "Lo", "La", "Nos", "Os", "Los", "Las", "Se", "Mi", "Mío", "Mía", "Míos", "Mías", "Tu", "Tuyo", "Tuya", "Tuyos", "Tuyas", "Su", "Suyo", "Suya", "Suyos", "Suyas", "Nuestro", "Nuestra", "Nuestros", "Nuestras", "Vuestro", "Vuestra", "Vuestros", "Vuestras", "Este", "Esta", "Estos", "Estas", "Ese", "Esa", "Esos", "Esas", "Aquel", "Aquella", "Aquellos", "Aquellas", "Alguno", "Alguna", "Algunos", "Algunas", "Ninguno", "Ninguna", "Ningunos", "Ningunas", "Uno", "Una", "Unos", "Unas", "Otro", "Otra", "Otros", "Otras", "Que", "Cual", "Quien", "Quienes", "Suyo", "Suya", "Suyos", "Suyas", "Usted", "Ustedes", "Vos"]

    #Ciclo para eliminar las stop words con ayuda de la categoria gramatical identificada por spacy y los diccionarios previamente definidos
    for lemma in doc2:
        if(lemma.pos_ != "DET" and lemma.pos_ != "ADP" and lemma.pos_ != "CONJ" and lemma.pos_ != "PRON" and lemma.text not in diccionario_articulos 
           and lemma.text not in diccionario_pronombres and lemma.text not in diccionario_preposiciones and lemma.text not in diccionario_conjunciones):  # "DET" es la etiqueta de POS para los artículos
            texto_limpio.append(lemma.text)

    #Juntar el texto sin stop words
    texto_resultado = " ".join(texto_limpio) 

    #Eliminar espacios extra
    texto_sin_espacios = re.sub('\s+', ' ', texto_resultado) 

    #Eliminar espacios al inicio de una linea
    texto_final = texto_sin_espacios.strip()

    #Escribir el texto en el archivo creado, linea por linea
    archivo_nuevo.write(texto_final + '\n')

archivo_nuevo.close() #Se cierra el archivo del nuevo corpus creado