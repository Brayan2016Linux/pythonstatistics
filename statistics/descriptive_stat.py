# -*- coding: utf-8 -*-
#!python
#descriptive_stat.py
#Created: 07/21/2017
#Last Updated: 07/21/2017

#/*******************************************************
#* Copyright (C) 2016-2017 Brayan Rodriguez D. <bradrd2009jp@gmail.com>
#* This file is part of Python Statistics.
#* Python Statistics can not be copied and/or distributed without the express
#* permission of Brayan Rodriguez
#*******************************************************/

#********************************************************
#*Conjunto de herramientas estadísticas para el análisis*
#*univariado, variables cuantitativas por medio de OOP  *
#*Desarrollado por Brayan Rodríguez                     *
#*Versión 1.2                                           *
#********************************************************

#Para importar librerías en carpetas aledañas a nivel superior del .py
#import sys
#sys.path.append("./<directorio>")
#import <modulo> as <alias>

#Para importar más de un módulo aledaño a nivel superior del .py
#import sys
#sys.path.append("./")
#from carpeta1 import <modulo> as <alias>
#from carpeta2 import <modulo> as <alias>

#importar librerías en subcarpetas al mismo nivel del .py
#from <carpeta> import <modulo> as <alias>

#Para importar la librería matemáticas
import math

#Devuelve el tamaño total de la lista
def number_of_values(my_list):
    """Calculate the number of values in a list
    
    Atributes
       my_list
       
    return number of values
    """
    return len(my_list)


#Devuelve el cuadrado de un número
def square_number(value):
    """Calculate the square of a number
    
    Atributes
        value
        
    return square of a number
    """
    return value * value

#Devuelve el valor de la suma de los valores del arreglo
def sum_of_values_X(my_list):
    """Calculate the sum of values of variable X
    
    Atributes
        my_list
        
    return sum of values of X
    """
    suma = 0
    i = 0
    while i < len(my_list):
        suma = suma + my_list[i]
        i = i + 1
    return suma

#Devuelve el valor de la suma de los cuadrados de los valores
#del arreglo
def sum_of_square_values_X(my_list):
    """Calculate the sum of square values of variable X
    
    Atributes
        my_list
        
    return sum of square values of X
    """
    suma = 0
    i = 0
    while i < len(my_list):
        suma = suma + square_number(my_list[i])
        i = i + 1
    return suma

#Devuelve la media aritmética
def arithmetic_mean(my_list):
    """Calculate the arithmetic mean of values of variable X
    
    Atributes
        my_list
        
    return arithmetic mean of values of X
    """
    suma = sum_of_values_X(my_list)
    return suma / len(my_list)

#Para crear una llamada interna en python debe de crearse
#un objeto de la clase para que este llame a la función
#internamente

#Devuelve la variancia sigma (n)
def variance_value_sigma(my_list):
    """Calculate the variance of values of variable X (population)
    
    Atributes
        my_list
        
    return variance of values of X
    """
    cuadSum = sum_of_square_values_X(my_list) / len(my_list)
    average = arithmetic_mean(my_list)
    cuadAverage = math.pow(average, 2)
    variance = cuadSum - cuadAverage
    return variance

#Devuelve la variancia normal (n - 1)
#Float (integer) convierte un entero en double
def variance_value_normal(my_list):
    """Calculate the variance of values of variable X (sample)
    
    Atributes
        my_list
        
    return variance of values of X
    """
    varSigma = variance_value_sigma(my_list)
    n = len(my_list)
    correctionFactor = float(n) / float(n - 1)
    varianceN = correctionFactor * varSigma
    return varianceN

#Devuelve la desviación estándar sigma (n)
def standard_desviation_sigma(my_list):
    """Calculate the standart desviation of values of variable X (population)
    
    Atributes
        my_list
        
    return standart desviation sigma of values of X
    """
    stdDesv = math.sqrt(variance_value_sigma(my_list))
    return stdDesv

#Devuelve la desviación estándar normal (n - 1)
def standard_desviation_normal(my_list):
    """Calculate the standart desviation of values of variable X (sample)
    
    Atributes
        my_list
        
    return standart desviation normal of values of X
    """
    stdDesv = math.sqrt(variance_value_normal(my_list))
    return stdDesv

#Devuelve el coeficiente de variación sigma (n)
def variation_coefficient_sigma(my_list):
    """Calculate the variation coefficient of values of variable X (population)
    
    Atributes
        my_list
        
    return variation coefficient sigma of values of X
    """
    average = arithmetic_mean(my_list)
    stdDesv = math.sqrt(variance_value_sigma(my_list))
    return stdDesv / average * 100

#Devuelve el coeficiente de variacion normal (n - 1)
def variation_coefficient_normal(my_list):
    """Calculate the variation coefficient of values of variable X (sample)
    
    Atributes
        my_list
        
    return variation coefficient normal of values of X
    """
    average = arithmetic_mean(my_list)
    stdDesv = math.sqrt(variance_value_normal(my_list))
    return stdDesv / average * 100

#Para darle formato a una salida se escribe
#print "String de salida {0: .<numerodecimales>f}".format(variable)

#Devuelve los valores de una lista ordenada
def ordered_values(my_list):
    """Return the values of a list sorted
    
    Atributes
        my_list
        
    return my_list sorted
    """
    #Orden por referencia: <orderedList> = sorted(<lista>)
    #Orden directo: <originalList>.sort()
    aux = sorted(my_list)
    return aux

#Devuelve la interpolación de un percentil
def percentile_interpolation(my_list, percentileIndex):
    """Calculate value of a percentil with interpolation
    
    Atributes
        my_list
        percentileIndex
        
    return values of a percentile
    """
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
    """Calculate value of a percentil R6
    
    Atributes
        my_list
        position
        
    return values of a percentile R6
    """
    aux = ordered_values(my_list)
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
            return percentile_interpolation(aux, percentileIndex)

#Devuelve el percentil R7 excel y calc
def percentileR7(my_list, position):
    """Calculate value of a percentil R7
    
    Atributes
        my_list
        position
        
    return values of a percentile R7
    """
    aux = ordered_values(my_list)
    p = position / 100.0
    N = len(my_list)
    percentileIndex = (N - 1.0) * p + 1.0
    if p == 1.0:
        return max_value(aux)
    else:
        return percentile_interpolation(aux, percentileIndex)

#Devuelve el percentil R8 Maple-7
def percentileR8(my_list, position):
    """Calculate value of a percentil R8
    
    Atributes
        my_list
        position
        
    return values of a percentile R8
    """
    aux = ordered_values(my_list)
    p = position / 100.0
    N = len(my_list)
    percentileIndex = (N + 1.0 / 3.0) * p + (1.0 / 3.0)
    infimus = (2.0 / 3.0) / (N + 1.0 / 3.0)
    supremus = (N - 1.0 / 3.0) / (N + 1.0 / 3.0)
    if p < infimus:
        return min_value(aux)
    else:
        if p >= supremus:
            return max_value(aux)
        else:
            return percentile_interpolation(aux, percentileIndex)

#Devuelve el promedio ponderado
def weighted_mean(my_list, my_weights):
    """Calculate a weighted mean with a list of values and a weights vector
    
    Atributes
        my_list
        my_weights --list
        
    return weighted mean
    """
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
def min_value(my_list):
    """Calculate minimum value of a list
    
    Atributes
        my_list
        
    return minimum value
    """
    aux = ordered_values(my_list)
    return aux[0]

#Devuelve el valor máximo de una lista
def max_value(my_list):
    """Calculate maximum value of a list
    
    Atributes
        my_list
        
    return maximum value
    """
    aux = ordered_values(my_list)
    return aux[len(aux) - 1]

#Devuelve el valor del percentil 25
def first_quartile(my_list):
    """Calculate first quartile value of a list
    
    Atributes
        my_list
        
    return firts quartile value
    """
    return percentileR7(my_list, 25)

#Devuelve el valor del percentil 50
def second_quartile(my_list):
    """Calculate second quartile value of a list
    
    Atributes
        my_list
        
    return second quartile value
    """
    return percentileR7(my_list, 50)

#Devuelve el valor del percentil 75
def third_quartile(my_list):
    """Calculate third quartile value of a list
    
    Atributes
        my_list
        
    return third quartile value
    """
    return percentileR7(my_list, 75)

#Devuelve el valor del percentil 100
def fourth_quartile(my_list):
    """Calculate fourth quartile value of a list
    
    Atributes
        my_list
        
    return fourth quartile value
    """
    return max_value(my_list)

#Devuelve la lista de todos los cuartiles
def quartile(my_list):
    """Return a list with all quartile values
    
    Atributes
        my_list
        
    return quartile values list
    """
    aux = []
    aux.append(min_value(my_list))
    aux.append(first_quartile(my_list))
    aux.append(second_quartile(my_list))
    aux.append(third_quartile(my_list))
    aux.append(fourth_quartile(my_list))
    return aux

#Devuelve el valor rango
def data_range(my_list):
    """Calculate data range of a list
    
    Atributes
        my_list
        
    return data range
    """
    datoMenor = min_value(my_list)
    datoMayor = max_value(my_list)
    return datoMayor - datoMenor

#Devuelve el valor de la mediana
def median_value(my_list):
    """Calculate median value of a list
    
    Atributes
        my_list
        
    return median value
    """
    return secondQuartile(my_list)

#Devuelve la variancia ponderada
def weighted_variance(my_list, weights):
    """Calculate the wighted variance of a list of values
    
    Atributes
        my_list
        weights --vector
        
    return values of a percentile R6
    """
    weightedmean = weighted_mean(my_list, weights)
    sumOfSquareValues = 0.0
    weightedList = []
    #Valores cuadrados
    for i in range(len(my_list)):
        mySquareW = square_number(my_list[i]) * weights[i]
        weightedList.append(mySquareW)
    #Suma de valores cuadrados
    for j in range(len(weightedList)):
        sumOfSquareValues = sumOfSquareValues + weightedList[j]
    #Variancia
    return sumOfSquareValues - square_number(weightedmean)

#Devuevle el valor normalizado de un dato
def normalized_value(value, average, stdDesv):
    """Calculate the normalized value (x-mean)/stdDesv
    
    Atributes
        value
        average
        stdDesv
        
    return normalized value
    """
    return float(value - average) / stdDesv
        
#Devuelve una lista de datos normalizados conociendo promedio y desviación
def normalized_list_of_data(quantitativeV, average, stdDesv):
    """Return a normalized list of data
    
    Atributes
        quantitativeV --list
        average
        stdDesv
        
    return normalized list of value
    """
    normalizedData = []
    for i in range(len(quantitativeV)):
        normalizedData.append(float(quantitativeV[i] - average) / stdDesv)
    return normalizedData
        
#Devuelve una lista de datos normalizados estimando promedio y desviacion
def normalized_list_T_Student(quantitativeV):
    """Return a normalized list of data directly
    
    Atributes
        quantitativeV --list
        average
        stdDesv
        
    return normalized list of value
    """
    average = arithmetic_mean(quantitativeV)
    stdDesv = standard_desviation_normal(quantitativeV)
    normalizedData = []
    for i in range(len(quantitativeV)):
        normalizedData.append(float(quantitativeV[i] - average) / stdDesv)
    return normalizedData
        
        
#Para llamado de función externa    
if __name__ == '__main__':
    print("You should import this one in your main project")
