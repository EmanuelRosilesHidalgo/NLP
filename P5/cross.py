
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import statistics
 
#Se carga el dataset de la iris plant desde sklearn
iris = load_iris()
 
#Se crea la variable para utilizar el K-Fold cross-validation estratificado con una semilla de 8 y valor de k = 10
skf = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 8)
 
#Se definen los valores de k que serán usados en el clasificador kNN
k = [1, 4, 7]
 
#Se crean las listas en donde se van a almacenar los valores de las métricas obtenidas en las 10 ejecuciones del K-Fold para posteriormente obtener su promedio
accuracy = list()
precision = list()
recall = list()
f1 = list()
 
print("Valores promedio de métricas\n")
for n in k: #Este ciclo va a iterar cada uno de los 3 valores de k para el kNN
    
    for train_index, test_index in skf.split(iris.data, iris.target): #Mediante este ciclo se realizan las 10 ejecuciones del K-Fold
        #Se obtienen los conjuntos de prueba y entrenamiento
        X_train, X_test = iris.data[train_index], iris.data[test_index]
        y_train, y_test = iris.target[train_index], iris.target[test_index]
        
        kNN = KNeighborsClassifier(n_neighbors = n) #Se crea la variable para aplicar el kNN con el valor de k correspondiente
        kNN.fit(X_train, y_train) #Se entrena al clasificador kNN con el conjunto de entrenamiento
        y_pred = kNN.predict(X_test) #Se predicen las clases con el conjunto de prueba
        
        #Se comparan las clases predichas con las reales y se van almacenando cada una de las métricas obtenidas de esa comparación en su respectiva lista
        accuracy.append(accuracy_score(y_test, y_pred)) #Exactitud
        precision.append(precision_score(y_test, y_pred, average="macro")) #Precisión
        recall.append(recall_score(y_test, y_pred, average="macro")) #Sensibilidad
        f1.append(f1_score(y_test, y_pred, average="macro")) #F1-score
 
    #Al terminar las 10 ejecuciones se obtiene el promedio de cada métrica y se muestran
    print(f'Para k = {n}')
    print(f'Exactitud: {statistics.mean(accuracy)}')
    print(f'Precisión: {statistics.mean(precision)}')
    print(f'Sensibilidad: {statistics.mean(recall)}')
    print(f'F1-score: {statistics.mean(f1)}\n')
 