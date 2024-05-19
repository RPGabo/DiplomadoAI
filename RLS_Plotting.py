import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def linear_reg(data):
    #Obtener los títulos del archivo
    x_label = data.columns[0]
    y_label = data.columns[1]

    #Separar las 2 últimas filas para usarlas de testeo
    X_predict = data.iloc[-2:, 0].values.reshape(-1, 1)
    y_predict_actual = data.iloc[-2:, 1].values.reshape(-1, 1)

    #Usar la información restante para el entrenamiento
    X = data.iloc[:-2, 0].values.reshape(-1, 1)
    y = data.iloc[:-2, 1].values.reshape(-1, 1)

    #Crear y entrenar el modelo de regresión lineal
    linear_reg = LinearRegression()
    linear_reg.fit(X, y)

    #Realizar predicciones usando el modelo de regresión lineal
    y_predict = linear_reg.predict(X)
    y_predictions = linear_reg.predict(X_predict)

    #Visualización de los datos originales en azul, las predicciones en verde, los resultados de testeo reales en naranja y la linea de regresión obtenida
    plt.scatter(X, y, color='blue', label='Puntos Entrenamiento')
    plt.plot(X, y_predict, color='red', label='Línea Regresión')
    plt.scatter(X_predict, y_predictions, color='green', label='Puntos Predecidos')
    plt.scatter(X_predict, y_predict_actual, color='orange', label='Puntos Reales')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('Linear Regression')
    plt.legend()
    plt.show()


#Importar los datos de un archivo CSV
data = pd.read_csv('Diplomado\\Regresión Lineal\\Dataset_1.csv') 
linear_reg(data)

#Importar los datos de un archivo CSV
data = pd.read_csv('Diplomado\\Regresión Lineal\\Dataset_2.csv') 
linear_reg(data)

#Importar los datos de un archivo CSV
data = pd.read_csv('Diplomado\\Regresión Lineal\\Dataset_3.csv') 
linear_reg(data)
