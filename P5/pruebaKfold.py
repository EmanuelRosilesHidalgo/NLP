import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df_normalizacion = pd.read_pickle('df_tokenizacion_lematizacion_emojis_final.pkl')
 
print(df_normalizacion)
 
features = ['Title_Opinion','acumuladopositivo', 'acumuladonegative']
numeric_features = ['acumuladopositivo', 'acumuladonegative']
 
 
X = df_normalizacion[features]
y = df_normalizacion['Polarity']
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
 
print(f'\nTamaño de X_train: {len(X_train)} documentos')
print(f'Tamaño de X_test: {len(X_test)} documentos')
print(f'Tamaño de y_train: {len(y_train)} etiquetas')
print(f'Tamaño de y_test: {len(y_test)} etiquetas\n')
 
vectorizer_title_opinion = CountVectorizer()
X_train_tfidf_title_opinion = vectorizer_title_opinion.fit_transform(X_train['Title_Opinion'])
X_test_tfidf_title_opinion = vectorizer_title_opinion.transform(X_test['Title_Opinion'])
 
X_train_final = hstack([X_train_tfidf_title_opinion, X_train[numeric_features].values])
X_test_final = hstack([X_test_tfidf_title_opinion, X_test[numeric_features].values])
 
clf_polarity = LogisticRegression(max_iter=10000)
clf_polarity.fit(X_train_final, y_train)
 
y_pred = clf_polarity.predict(X_test_final)
 
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
 
print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(classification_rep)

