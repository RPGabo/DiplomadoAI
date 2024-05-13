from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack
import pandas as pd
import time

def ID3(X_ID3_train, y_ID3_train):
    #Crear el clasificador de árlbol de desición ID3
    id3_classifier = DecisionTreeClassifier(criterion='entropy')
    #Entrenar el clasificador
    id3_classifier.fit(X_ID3_train, y_ID3_train)
    return id3_classifier

def Naive_Bayes(X_NB_train, y_NB_train):
    #Crear el clasificador Naive Bayes Multinomial
    mnb_classifier = MultinomialNB()
    #Entrenar el clasificador
    mnb_classifier.fit(X_NB_train, y_NB_train)
    return mnb_classifier


#Conjunto de datos del ejercicio "Play Golf"
data = pd.DataFrame({
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cold','Cold','Cold','Mild','Cold','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
    'Windy': ['False','True','False','False','False','True','True','False','False','False','True','True','False','True'],
    'Play Golf': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
})

#Separar la información en entradas (X) y objetivos (y)
X = data.drop('Play Golf', axis=1)
y = data['Play Golf']

#Preprocesar la información para ID3
label_encoder = LabelEncoder()
X_ID3 = pd.DataFrame()
for column in X.columns:
    X_ID3[column] = label_encoder.fit_transform(X[column])
    
y_ID3 = label_encoder.fit_transform(y)

#Preprocesar la información para MNB
X_list = []
vectorizers = []
for column in X.columns:
    vectorizer = CountVectorizer()
    vectorizers.append(vectorizer)
    X_column = vectorizer.fit_transform(X[column])
    X_list.append(X_column)
X_NB = hstack(X_list)
    
y_NB = label_encoder.fit_transform(y)


#Separar la información en sets de entrenamiento y testeo
X_ID3_train, X_ID3_test, y_ID3_train, y_ID3_test = train_test_split(X_ID3, y_ID3, test_size=0.2, random_state=42)
X_NB_train, X_NB_test, y_NB_train, y_NB_test = train_test_split(X_NB, y_NB, test_size=0.2, random_state=42)


#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de ID3
ID3_classifier = ID3(X_ID3_train, y_ID3_train)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_ID3 = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Naive Bayes Multinomial
MNB_classifier = Naive_Bayes(X_NB_train, y_NB_train)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_MNB = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Imprimir resultados
print(f"Tiempo de entrenamiento del Clasificador ID3: {tiempo_total_ID3} s")
print(f"Tiempo de entrenamiento del Clasificador Naive Bayes Multinomial: {tiempo_total_MNB} s")

#Medición de Precisiones
#ID3
accuracy = ID3_classifier.score(X_ID3_test, y_ID3_test)
print("Precisión ID3:", accuracy)
#MNB
y_pred_NB = MNB_classifier.predict(X_NB_test)
accuracy = accuracy_score(y_NB_test, y_pred_NB)
print("Precisión MNB:", accuracy)


#Probar los resultados con el mismo set de entrada
test_example = pd.DataFrame({
    'Outlook': ['Overcast'], 
    'Temperature': ['Mild'], 
    'Humidity': ['Normal'], 
    'Windy': ['False']
    })

#ID3
test_example_ID3 = test_example.apply(label_encoder.fit_transform)
predicted_class = ID3_classifier.predict(test_example_ID3)
if predicted_class[0] == 1:
    print("Prediction ID3: Yes (Play Golf)")
else:
    print("Prediction ID3: No (Don't Play Golf)")

#MNB
test_list = []
for i, column in enumerate(test_example.columns):
    #Usar la misma vectorización de la columna correspondiente durante el entrenamiento
    vectorizer = vectorizers[i]
    test_example_columns = vectorizer.transform(test_example[column])
    test_list.append(test_example_columns)
test_example_MNB = hstack(test_list)

predicted_class = MNB_classifier.predict(test_example_MNB)
if predicted_class[0] == 1:
    print("Prediction MNB: Yes (Play Golf)")
else:
    print("Prediction MNB: No (Don't Play Golf)")