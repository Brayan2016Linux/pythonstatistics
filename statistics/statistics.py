# -*- coding: utf-8 -*-
#!python
#statistics.py

#/*******************************************************
#* Copyright (C) 2016-2017 Brayan Rodriguez D. <bradrd2009jp@gmail.com>
#* 
#* This file is part of Python Statistics.
#* 
#* Python Statistics can not be copied and/or distributed without the express
#* permission of Brayan Rodriguez
#*******************************************************/

#********************************************************
#*Conjunto de herramientas estadísticas para el análisis*
#*univariado, variables cuantitativas                   *
#*Desarrollado por Brayan Rodríguez                     *
#*Versión 1.2                                           *
#********************************************************

#Para importar la librería matemáticas
import math

#Importa la libreria utilizando el nombre, no se utiliza con class:
#if __name__ == '__main__':



#Devuelve el cuadrado de un número
def squareNumber(value):
    return value * value

#Devuelve el valor de la suma de los valores del arreglo
def sumValueX(my_list):
    suma = 0
    i = 0
    while i < len(my_list):
        suma = suma + my_list[i]
        i = i + 1
    return suma

#Devuelve el valor de la suma de los cuadrados de los valores
#del arreglo
def sumSquareValueX(my_list):
    suma = 0
    i = 0
    while i < len(my_list):
        suma = suma + squareNumber(my_list[i])
        i = i + 1
    return suma

#Devuelve la media aritmética
def arithmeticMean(my_list):
    suma = sumValueX(my_list)
    return suma / len(my_list)

#Para crear una llamada interna en python debe de crearse
#un objeto de la clase para que este llame a la función
#internamente

#Devuelve la variancia sigma (n)
def varianceValueSigma(my_list):
    cuadSum = sumSquareValueX(my_list) / len(my_list)
    average = arithmeticMean(my_list)
    cuadAverage = math.pow(average, 2)
    variance = cuadSum - cuadAverage
    return variance

#Devuelve la variancia normal (n - 1)
#Float (integer) convierte un entero en double
def varianceValueNormal(my_list):
    varSigma = varianceValueSigma(my_list)
    n = len(my_list)
    correctionFactor = float(n) / float(n - 1)
    varianceN = correctionFactor * varSigma
    return varianceN

#Devuelve la desviación estándar sigma (n)
def standardDesviationSigma(my_list):
    stdDesv = math.sqrt(varianceValueSigma(my_list))
    return stdDesv

#Devuelve la desviación estándar normal (n - 1)
def standardDesviationNormal(my_list):
    stdDesv = math.sqrt(varianceValueNormal(my_list))
    return stdDesv

#Devuelve el coeficiente de variación sigma (n)
def variationCoefficientSigma(my_list):
    average = arithmeticMean(my_list)
    stdDesv = math.sqrt(varianceValueSigma(my_list))
    return stdDesv / average * 100

#Devuelve el coeficiente de variacion normal (n - 1)
def variationCoefficientNormal(my_list):
    average = arithmeticMean(my_list)
    stdDesv = math.sqrt(varianceValueNormal(my_list))
    return stdDesv / average * 100

#Para darle formato a una salida se escribe
#print "String de salida {0: .<numerodecimales>f}".format(variable)

#Devuelve los valores de una lista ordenada
def orderedValues(my_list):
    #Orden por referencia: <orderedList> = sorted(<lista>)
    #Orden directo: <originalList>.sort()
    aux = sorted(my_list)
    return aux

#Devuelve la interpolación de un percentil
def percentileInterpolation(my_list, percentileIndex):
    #Obtener limites superior e inferior
    beforePos = int(math.floor(percentileIndex))
    afterPos = beforePos + 1
    #Linear interpolation
    factorSlope = (percentileIndex - beforePos) / (afterPos - beforePos)
    IntervalRange = my_list[afterPos - 1] - my_list[beforePos - 1]
    percentile = my_list[beforePos - 1] + factorSlope * IntervalRange
    return percentile

#Devuelve el percentil R6 académico
def percentileR6(my_list, position):
    aux = orderedValues(my_list)
    p = position / 100.0
    N = len(my_list)
    percentileIndex = p * (N + 1.0)
    infimus = 1.0 / (N + 1.0)
    supremus = N / (N + 1.0)
    if p < infimus:
        return minValue(aux)
    else:
        if p >= supremus:
            return maxValue(aux)
        else:
            return percentileInterpolation(aux, percentileIndex)

#Devuelve el percentil R7 excel y calc
def percentileR7(my_list, position):
    aux = orderedValues(my_list)
    p = position / 100.0
    N = len(my_list)
    percentileIndex = (N - 1.0) * p + 1.0
    if p == 1.0:
        return maxValue(aux)
    else:
        return percentileInterpolation(aux, percentileIndex)

#Devuelve el percentil R8 Maple-7
def percentileR8(my_list, position):
    aux = orderedValues(my_list)
    p = position / 100.0
    N = len(my_list)
    percentileIndex = (N + 1.0 / 3.0) * p + (1.0 / 3.0)
    infimus = (2.0 / 3.0) / (N + 1.0 / 3.0)
    supremus = (N - 1.0 / 3.0) / (N + 1.0 / 3.0)
    if p < infimus:
        return minValue(aux)
    else:
        if p >= supremus:
            return maxValue(aux)
        else:
            return percentileInterpolation(aux, percentileIndex)

#Devuelve el promedio ponderado
def weightedMean(my_list, my_weights):
    sumOfWeights = 0.0
    sumOfWeightedValues = 0.0
    weightedList = []
    for i in range(len(my_weights)):
        sumOfWeights = sumOfWeights + my_weights[i - 1]
    for i in range(len(my_list)):
        weightedList.append(my_list[i - 1] * my_weights[i - 1])
    for i in range(len(weightedList)):
        sumOfWeightedValues = sumOfWeightedValues + weightedList[i - 1]
    return sumOfWeightedValues / sumOfWeights

#Devuelve el valor minimo de una lista
def minValue(my_list):
    aux = orderedValues(my_list)
    return aux[0]

#Devuelve el valor máximo de una lista
def maxValue(my_list):
    aux = orderedValues(my_list)
    return aux[len(aux) - 1]

#Devuelve el valor del percentil 25
def firstQuartile(my_list):
    return percentileR7(my_list, 25)

#Devuelve el valor del percentil 50
def secondQuartile(my_list):
    return percentileR7(my_list, 50)

#Devuelve el valor del percentil 75
def thirdQuartile(my_list):
    return percentileR7(my_list, 75)

#Devuelve el valor del percentil 100
def fourthQuartile(my_list):
    return maxValue(my_list)

#Devuelve la lista de todos los cuartiles
def quartile(my_list):
    aux = []
    aux.append(minValue(my_list))
    aux.append(firstQuartile(my_list))
    aux.append(secondQuartile(my_list))
    aux.append(thirdQuartile(my_list))
    aux.append(fourthQuartile(my_list))
    return aux

#Devuelve el valor rango
def dataRange(my_list):
    datoMenor = minValue(my_list)
    datoMayor = maxValue(my_list)
    return datoMayor - datoMenor

#Devuelve el valor de la mediana
def medianValue(my_list):
    return datosMediana.secondQuartile(my_list)

#Devuelve la variancia ponderada
def weightedVariance(my_list, weights):
    weightedmean = weightedMean(my_list, weights)
    sumOfSquareValues = 0.0
    weightedList = []
    #Valores cuadrados
    for i in range(len(my_list)):
        mySquareW = squareNumber(my_list[i]) * weights[i]
        weightedList.append(mySquareW)
    #Suma de valores cuadrados
    for j in range(len(weightedList)):
        sumOfSquareValues = sumOfSquareValues + weightedList[j]
    #Variancia
    return sumOfSquareValues - squareNumber(weightedmean)

#Devuevle el valor normalizado de un dato
def normalizedValue(value, average, stdDesv):
    return float(value - average) / stdDesv
        
#Devuelve una lista de datos normalizados conociendo promedio y desviación
def normalizedListOfData(quantitativeV, average, stdDesv):
    normalizedData = []
    for i in range(len(quantitativeV)):
        normalizedData.append(float(quantitativeV[i] - average) / stdDesv)
    return normalizedData
        
#Devuelve una lista de datos normalizados estimando promedio y desviacion
def normalizedListTStudent(quantitativeV):
    average = arithmeticMean(quantitativeV)
    stdDesv = standardDesviationNormal(quantitativeV)
    normalizedData = []
    for i in range(len(quantitativeV)):
        normalizedData.append(float(quantitativeV[i] - average) / stdDesv)
    return normalizedData
        
        
#Para llamado de función externa    
if __name__ == '__main__':
    print("You should import this one in your main project")
