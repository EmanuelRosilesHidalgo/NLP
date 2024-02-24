import pickle
import re

def getSELFeatures(cadenas, lexicon_sel, lexicon_emoji):

	#'hastiar': [('Enojo\n', '0.629'), ('Repulsi\xf3n\n', '0.596')]
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
				print(palabra)
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
				print(palabra)
				caracteristicas2 = lexicon_emoji[palabra]
				for polaridad, valor in caracteristicas2:
					print(valor)
					if polaridad == 'positive':
						valor_positivo = valor_positivo + float(valor)
					elif polaridad == 'negative':
						valor_negativo = valor_negativo + float(valor)


		dic['__positive__'] = valor_positivo
		dic['__negative__'] = valor_negativo
		dic['__alegria__'] = valor_alegria
		dic['__tristeza__'] = valor_tristeza
		dic['__enojo__'] = valor_enojo
		dic['__repulsion__'] = valor_repulsion
		dic['__miedo__'] = valor_miedo
		dic['__sorpresa__'] = valor_sorpresa
		
		#Esto es para los valores acumulados del mapeo a positivo (alegría + sorpresa) y negativo (enojo + miedo + repulsión + tristeza)
		dic['acumuladopositivo'] = dic['__alegria__'] + dic['__sorpresa__'] + dic['__positive__']
		dic['acumuladonegative'] = dic['__enojo__'] + dic['__miedo__'] + dic['__repulsion__'] + dic['__tristeza__'] + dic['__negative__']

	

		features.append (dic)
	
	
	return features

def process_row(row, lexicon_sel, lexicon_emoji):
    polaridad = getSELFeatures([row['Title_Opinion']], lexicon_sel, lexicon_emoji)
    return polaridad[0] if polaridad else None

cadena = "Parece un castillo	Ideal para subir las escalinatas y divisar su linda vista panoramica de la ciudad. recomiendo visitarla de noche cuando esta iluminada.	5	Attractive"

with open('lexicon_emoji.pkl', 'rb') as archivo_pickle:
    lexicon_emoji = pickle.load(archivo_pickle)
	
with open('lexicon_sel.pkl', 'rb') as archivo_pickle2:
		lexicon_sel = pickle.load(archivo_pickle2)
		
resultados = getSELFeatures([cadena], lexicon_sel, lexicon_emoji)
print(resultados)


"""cadena = "😄"

with open('lexicon_emoji.pkl', 'rb') as archivo_pickle:
    lexicon = pickle.load(archivo_pickle)

detectar_emoji(lexicon, cadena)"""