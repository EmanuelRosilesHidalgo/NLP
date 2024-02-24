import pandas as pd
from sklearn.calibration import cross_val_predict
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.sparse import hstack, csr_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, make_scorer, f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC


df_normalizacion = pd.read_pickle('df_tokenizacion_lematizacion_emojis_final.pkl')

features = ['Title_Opinion', 'acumuladopositivo', 'acumuladonegative']
numeric_features = ['acumuladopositivo', 'acumuladonegative']

X = df_normalizacion[features]
y = df_normalizacion['Polarity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print(f'\nTamaño de X_train: {len(X_train)} documentos')
print(f'Tamaño de X_test: {len(X_test)} documentos')
print(f'Tamaño de y_train: {len(y_train)} etiquetas')
print(f'Tamaño de y_test: {len(y_test)} etiquetas\n')

# Vectorización de texto
vectorizer_title_opinion = CountVectorizer()
X_train_vectorizer = vectorizer_title_opinion.fit_transform(X_train['Title_Opinion'])
X_test_vectorizer = vectorizer_title_opinion.transform(X_test['Title_Opinion'])

# Combinar características numéricas y vectorizadas
X_train_final = hstack([X_train_vectorizer, csr_matrix(X_train[numeric_features].values)])
X_test_final = hstack([X_test_vectorizer, csr_matrix(X_test[numeric_features].values)])

# Inicializar el clasificador SVM
clf_polarity = SVC(kernel='linear')

# Inicializar KFold con el número deseado de divisiones (folds)
kf = KFold(n_splits=5, shuffle=True, random_state=0)

# Definir la métrica F1-score para la validación cruzada
scoring_metric = make_scorer(f1_score, average='macro')

# Aplicar la validación cruzada y obtener las puntuaciones
cv_scores = cross_val_score(clf_polarity, X_train_final, y_train, cv=kf, scoring=scoring_metric)

# Imprimir las puntuaciones de validación cruzada
print("Puntuaciones de Validación Cruzada (F1-score):", cv_scores)

# Imprimir la puntuación media y la desviación estándar de las puntuaciones
print("F1-score Promedio:", cv_scores.mean())

