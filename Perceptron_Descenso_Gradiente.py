#Importar la libreria para medir el tiempo
import time
#Importar la libreria para los arreglos
import numpy as np
#Importar la libreria para las operaciones del Perceptron
from sklearn.linear_model import Perceptron, SGDClassifier


#Definición de la función del Perceptrón Simple
def Perceptron_Simple(training_data,labels):
    #Creación del modelo simple, especificando el learning rate y la cantidad máxima de iteraciones
    perceptron = Perceptron(eta0=1, max_iter=100)
    #Entrenamiento del Perceptrón
    perceptron.fit(training_data, labels)


#Definición de la función del Perceptrón Simple con el descenso de gradiente (SGD)
def Perceptron_SGD(training_data,labels):
    #Creación del modelo SGD, especificando un Learning rate constante y la cantidad máxima de iteraciones
    perceptron_sgd = SGDClassifier(eta0=1, learning_rate="constant", max_iter=1000)
    #Entrenamiento del Perceptrón con SGD
    perceptron_sgd.fit(training_data,labels)


#Definición de la función del Perceptrón Simple con el descenso de gradiente (SGD)
def Perceptron_SGD_ext(training_data,labels):
    #Creación del modelo SGD, especificando un Learning rate óptimo, la pérdida, la cantidad máxima de iteraciones y la tolerancia
    perceptron_sgd_extendido = SGDClassifier(loss="perceptron", eta0=1, learning_rate="optimal", max_iter=1000, tol=0.001)
    #Entrenamiento del Perceptrón con SGD
    perceptron_sgd_extendido.fit(training_data,labels)



#Creación de las coordendas de entrenamiento de la compuerta lógica AND
training_data_AND = [[0,0], [1,0], [0,1], [1,1]]
#Definiición de las etiquetas de salida como Array de la compuerta lógica AND
labels_AND = np.array([0,0,0,1]) #Clase 1: 1, Clase 2: 0

#Creación de las coordendas de entrenamiento de la compuerta lógica OR
training_data_OR = [[0,0], [1,0], [0,1], [1,1]]
#Definiición de las etiquetas de salida como Array de la compuerta lógica OR
labels_OR = np.array([0,1,1,1]) #Clase 1: 1, Clase 2: 0



#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Perceptrón Simple
Perceptron_Simple(training_data_AND,labels_AND)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_simple_AND = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Perceptrón Simple SGD
Perceptron_SGD(training_data_AND,labels_AND)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_GSD_AND = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Perceptrón Simple SGD ext
Perceptron_SGD_ext(training_data_AND,labels_AND)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_GSD_AND_ext = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Imprimir resultados
print(f"Tiempo de entrenamiento del Perceptrón Simple para la compuerta lógica AND: {tiempo_total_simple_AND} s")
print(f"Tiempo de entrenamiento del Perceptrón Simple con Descenso de Gradiente Estocástico (GSD) para la compuerta lógica AND: {tiempo_total_GSD_AND} s")
print(f"Tiempo de entrenamiento del Perceptrón Simple con Descenso de Gradiente Estocástico (GSD) ext para la compuerta lógica AND: {tiempo_total_GSD_AND_ext} s")

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Perceptrón Simple
Perceptron_Simple(training_data_OR,labels_OR)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_simple_OR = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Perceptrón Simple SGD
Perceptron_SGD(training_data_OR,labels_OR)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_GSD_OR = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de Perceptrón Simple SGD ext
Perceptron_SGD_ext(training_data_OR,labels_OR)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_GSD_OR_ext = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Imprimir resultados
print(f"Tiempo de entrenamiento del Perceptrón Simple para la compuerta lógica OR: {tiempo_total_simple_OR} s")
print(f"Tiempo de entrenamiento del Perceptrón Simple con Descenso de Gradiente Estocástico (GSD) para la compuerta lógica OR: {tiempo_total_GSD_OR} s")
print(f"Tiempo de entrenamiento del Perceptrón Simple con Descenso de Gradiente Estocástico (GSD) ext para la compuerta lógica OR: {tiempo_total_GSD_OR_ext} s")
