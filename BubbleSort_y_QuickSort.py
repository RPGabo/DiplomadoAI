#Importar la libreria para medir el tiempo
import time
#Importar la libreria para generar la lista
import random

#Definición de la función que genera la lista de n elementos solo decimales
def generar_lista_decimales(n):
    #Crear una lista vacia
    lista = []
    #Crear un ciclo de n repeticiones
    for i in range(n):
        #En cada iteración se agregará un número aleatorio en el rango especificado.
        lista.append(random.uniform(0.0,float(n)))
    #Retornar la lista generada    
    return lista

#Definición de la función que genera la lista de n elementos solo decimales
def generar_lista_mezclada(n):
    #Crear una lista vacia
    lista = []
    #Crear un ciclo de n repeticiones
    for i in range(n):
        #En cada iteración se agregará un número aleatorio en el rango especificado.
        #Se genera una desición aleatoria de True o False
        if random.choice([True, False]):
            #Si la desición aleatoria es True entonces se agrega un número entero en el rango especificado
            lista.append(random.randint(0, n))
        else:
            #Si la desición aleatoria es False entonces se agrega un número decimal en el rango especificado
            lista.append(random.uniform(0.0,float(n)))
    #Retornar la lista generada    
    return lista

#Definición de la función que recibe la lista a ordenar mediante el método Burbuja
def BubbleSort(lista):
    #Calcular la longitud de la lista
    longitud = len(lista)
    #Recorrer la lista completa por primera vez (Se resta uno porque la variable inicial empieza en 0)
    for inicial in range(longitud - 1):
        #Segundo recorrido de la lista hasta uno antes de la posición inicial
        for actual in range(longitud - 1 - inicial):
            #Calcular la posición siguiente a la actual para comparar
            siguiente = actual + 1
            #Comparar el dato actual con el siguiente
            if lista[actual] > lista[siguiente]:
                #Intercambiar los elementos si el actual es mayor que el siguiente
                lista[siguiente],lista[actual] = lista[actual],lista[siguiente]

#Definición de la función que retorna la mediana de 3 números dados
def middleOfThree(a,b,c):
    #Si la mediana corresponde al número del medio entonces retorna b
    if ((a < b and b < c) or (c < b and b < a)):
        return b
    #Si la mediana corresponde al número del inicio entonces retorna a
    elif ((b < a and a < c) or (c < a and a < b)):
        return a
    #sino entonces retorna c
    else:
        return c
    
#Definición de la función que recibe la lista a ordenar mediante el método Rápido
def QuickSort(lista_q):
    #Elegir el pivote
    if len(lista_q) > 2:
        #Si hay más de 2 elementos, el pivote es el elemente del medio entre el primer elemento, el último y el del medio de la lista 
        pivote = middleOfThree(lista_q[0], lista_q[len(lista_q)-1], lista_q[(len(lista_q)-1)//2])
    elif len(lista_q) == 2:
        #Si hay exactamente 2 elementos, el pivote es el primer elemento de la lista
        pivote = lista_q[0]
    else: 
        #si hay n solo elemento entonces el pivote debe ser él mismo
        return lista_q

    menores = []
    mayores = []
    iguales = []

    for item in lista_q:
        if item < pivote:
            menores.append(item)
        elif item == pivote:
            iguales.append(item)
        else:
            mayores.append(item)

    return QuickSort(menores) + iguales + QuickSort(mayores)

#llamar la función para generar la lista del caso 1
lista_org = generar_lista_decimales(500)
#llamar la función para generar la lista del caso 2
#lista_org = generar_lista_mezclados(1000)
#llamar la función para generar la lista del caso 3
#lista_org = generar_lista_mezclados(10000)
#Copiar la lista generada 2 veces, una para cada método de ordenamiento
lista_bubble = lista_org.copy()

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de ordenamiento burbuja
BubbleSort(lista_bubble)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_BubbleSort = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Tomar el registro de tiempo inicial
tiempo_inicial = time.time()
#Llamar la función de ordenamiento rápido
lista_quick=QuickSort(lista_org)
#Tomar el registro de tiempo final
tiempo_final = time.time()
#Calcular el tiempo de ejecución y darle formato para ver 20 posiciones decimales
tiempo_total_Quicksort = "{:.20f}".format(tiempo_final - tiempo_inicial)

#Imprimir resultados
print(f"La lista original: {lista_org}")
print(f"La lista ordenada por BubbleSort: {lista_bubble}")
print(f"La lista ordenada por QuickSort: {lista_quick}")
print(f"Tiempo de Ejecución del ordenamiento por método BubbleSort: {tiempo_total_BubbleSort} s")
print(f"Tiempo de Ejecución del ordenamiento por método QuickSort: {tiempo_total_Quicksort} s")


