import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
import spacy
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InterfazNormalizacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Document similarity")


        self.prueba_label = tk.Label(ventana, text="Selecciona el archivo de prueba")
        self.prueba_label.pack(padx=20, pady=10)

        self.prueba_entry = tk.Entry(ventana, width=40)
        self.prueba_entry.pack(padx=20, pady=10)

        self.prueba_boton = tk.Button(ventana, text="Seleccionar Prueba", command=self.seleccionar_prueba)
        self.prueba_boton.pack(padx=20, pady=10)

        self.seleccion_label = tk.Label(ventana, text="Selecciona la opción:")
        self.seleccion_label.pack(padx=20, pady=10)

        self.opcion_seleccionada = tk.StringVar()
        
        self.opcion_seleccionada.set("Frecuencia")
        
        self.radio_binaria = tk.Radiobutton(ventana, text="Binaria", variable=self.opcion_seleccionada, value="Binaria")
        self.radio_binaria.pack(padx=20, pady=5)

        self.radio_frecuencia = tk.Radiobutton(ventana, text="Frecuencia", variable=self.opcion_seleccionada, value="Frecuencia")
        self.radio_frecuencia.pack(padx=20, pady=5)

        self.radio_tfidf = tk.Radiobutton(ventana, text="TF-IDF", variable=self.opcion_seleccionada, value="TF-IDF")
        self.radio_tfidf.pack(padx=20, pady=5)

        self.ejecutar_boton = tk.Button(ventana, text="Ejecutar", command=self.ejecutar_normalizacion)
        self.ejecutar_boton.pack(pady=20)

        self.borrar_boton = tk.Button(ventana, text="Limpiar", command=self.borrar_texto)
        self.borrar_boton.pack(pady=10)

        self.resultado_label = tk.Label(ventana, text="Resultado:")
        self.resultado_label.pack(padx=20, pady=10)

        self.resultado_text = scrolledtext.ScrolledText(ventana, width=60, height=15)
        self.resultado_text.pack(padx=20, pady=10)


    def seleccionar_prueba(self):
        archivo_prueba = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        self.prueba_entry.delete(0, tk.END)
        self.prueba_entry.insert(0, archivo_prueba)

    def borrar_texto(self):
        # Función para borrar el texto del cuadro de texto
        self.resultado_text.delete(1.0, tk.END)

    def normalizar_texto(self, texto):
        nlp = spacy.load("es_core_news_sm")
        # Aquí deberías incluir el código de normalización que se encuentra en tu función original
        
        for linea in texto:
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

    def ejecutar_normalizacion(self):
        archivo_prueba = self.prueba_entry.get()  # Obtener la ruta del archivo desde el campo de entrada (si aún deseas obtenerla desde el campo)
        opcion_seleccionada = self.opcion_seleccionada.get()

        # Verificar si se seleccionó un archivo
        if not archivo_prueba:
            messagebox.showerror("Error", "Por favor, selecciona un archivo de prueba.")
            return  # Salir de la función si no se seleccionó un archivo

        # Leer el contenido del archivo seleccionado
        try:
            with open(archivo_prueba, 'r', encoding='utf-8') as archivo:
                contenido_archivo = archivo.readlines()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
            return  # Salir de la función en caso de error

        # Normalizar el contenido del archivo
        noticia_normalizada = self.normalizar_texto(contenido_archivo)
        nlp = spacy.load("es_core_news_sm")

        noticias = []

        with open('D:\\Python\\NLP\\P3\\corpus_normalizado.txt', 'r', encoding='utf-8') as archivo:
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
        
        opcion_elegida = opcion_seleccionada

        if opcion_elegida == "Binaria":
            representacion_vectorial_nueva_noticia = vectorizer.transform([noticia_normalizada])
            df_representacion_binaria_nueva_noticia = pd.DataFrame(representacion_vectorial_nueva_noticia.toarray(), columns=vectorizer.get_feature_names_out())
            similitud_coseno = cosine_similarity(representacion_vectorial_nueva_noticia, representacion_binaria)
            
        elif opcion_elegida == "Frecuencia":
            representacion_vectorial_nueva_noticia = count_vectorizer.transform([noticia_normalizada])
            df_representacion_frecuencia_nueva_noticia = pd.DataFrame(representacion_vectorial_nueva_noticia.toarray(), columns=count_vectorizer.get_feature_names_out()) 
            similitud_coseno = cosine_similarity(representacion_vectorial_nueva_noticia, representacion_frecuencia)
            
        elif opcion_elegida == "TF-IDF":
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
        df_similitud = df_similitud.reset_index()
        df_resultado = df_similitud.loc[0:9, ('Documento','Similitud')]
        df_resultado.index += 1 


        # Mostrar la prueba seleccionada (?)
        resultado = f"Prueba:\n{opcion_elegida}\n\nResultados de similitud:\n{df_resultado}"
        self.resultado_text.delete(1.0, tk.END)  # Borra el texto existente antes de agregar el resultado
        self.resultado_text.insert(tk.END, resultado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazNormalizacion(ventana)
    ventana.mainloop()