# -*- coding: utf-8 -*-
#!python
#frecuency.py
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

#Importa la libreria utilizando el nombre:
#if __name__ == '__main__':

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

#Para importar la librería
import math

import sys
sys.path.append("./")
from matrix import matrix as mat
from statistics import descriptive_stat as ds

#Default precision:
precision = 2

#configuración de la precisión
def set_precision(myprecision):
    """Set the number of decimals in output
    
    Atributes
       myprecision
       
    return --
    """
    precision = myprecision

#Devuelve el valor de la precisión
def get_precision():
    """Return defined number of decimals of output
    
    Atributes
       --
       
    return precision
    """
    return precision

#Devuelve el valor del límite de seguridad
def asurance_limit_value():
    """Calculate the limit value according with the precision
    
    Atributes
       --
       
    return asurance value
    """
    mypower = 5 * math.pow(10, - (get_precision() + 1))
    return mypower

#Devuelve la amplitud de las clases
def class_range(my_list, classNumber):
    """Calculate the class range value of a list
    
    Atributes
       my_list
       
    return class range value
    """
    myNumber = ds.data_range(my_list) / float(classNumber)
    setPrecision = "{0:0." + str(get_precision() - 1) + "f}"
    myString = ""
    myString = setPrecision.format(myNumber) + "5"
    return float(myString)

#Devuelve el límite inferior de una clase
def inferior_limit_class_value(my_list, classNumber):
    """Calculate the inferior limit value of a class
    
    Atributes
       my_list
       classNumber
       
    return inferior limit value of a class
    """
    firstValue = ds.min_value(my_list)
    classRangeValue = class_range(my_list, classNumber)
    addValue = firstValue - asurance_limit_value()
    setPrecision = "{0:0." + str(get_precision()) + "f}"
    myLimitsList = []
    for i in range(classNumber):
        myLimitsList.append(float(setPrecision.format(addValue)))
        addValue = addValue + classRangeValue
    return myLimitsList

#Devuelve el límite superior de una clase
def superior_limit_class_value(my_list, classNumber):
    """Calculate the superior limit value of a class
    
    Atributes
       my_list
       classNumber
       
    return superior limit value of a class
    """
    firstValue = ds.min_value(my_list)
    classRangeValue = class_range(my_list, classNumber)
    addValue = firstValue + classRangeValue - asurance_limit_value()
    setPrecision = "{0:0." + str(get_precision()) + "f}"
    myLimitsList = []
    for i in range(classNumber):
        myLimitsList.append(float(setPrecision.format(addValue)))
        addValue = addValue + classRangeValue
    return myLimitsList

#Devuelve la frequencia de la clase
def quantitative_frequency(my_list, classNumber):
    """Return a vector with quantitative frequency of each class
    
    Atributes
       my_list
       classNumber
       
    return quantitative frequency
    """
    linfC = inferior_limit_class_value(my_list, classNumber)
    lsupC = superior_limit_class_value(my_list, classNumber)
    #Lista a devolver
    frequency = []
    #Primer ciclo
    for i in range(classNumber):
        infLimit = linfC[i]
        supLimit = lsupC[i]
        count = 0
        #Segundo ciclo
        for j in range(len(my_list)):
            if my_list[j] >= infLimit:
                if my_list[j] < supLimit:
                    count = count + 1
        frequency.append(count)
    #Return
    return frequency

#Devuelve la clasificación de las variables cualitativas
def qualitative_classes(my_list):
    """Return a vector with quantitative class labels
    
    Atributes
       my_list
       
    return quanlitative class labels list
    """
    classList = []
    addValue = ""
    comprobator = True
    for i in range(len(my_list)):
        addValue = my_list[i]
        for j in range(len(classList)):
            if classList[j] == my_list[i]:
                comprobator = False
                break
            else:
                comprobator = True
        if comprobator is True:
            classList.append(addValue)
    return classList

#Devuelve la frecuencia de las variables
def qualitative_frequency(my_list):
    """Return a vector with quanlitative frequency of each class
    
    Atributes
       my_list
       
    return qualitative frequency
    """
    classList = qualitative_classes(my_list)
    freqList = []
    for i in range(len(classList)):
        freqList.append(my_list.count(classList[i]))
    return freqList

#Devuelve la matriz de contingencias
def contingency_frequency_matrix(firstVariable, secondVariable):
    """Return contingency matrix of frequency for two groups of
    qualitative variables
    
    Atributes
       firstVariable
       secondVariable
       
    return qualitative frequency matrix
    """
    #Total de observaciones
    N = len(firstVariable)
    #Clasificación
    RowClass = qualitative_classes(firstVariable)
    ColumnClass = qualitative_classes(secondVariable)
    numberRows = len(RowClass)
    numberCols = len(ColumnClass)
    #Matriz de contingencia
    contingencyMatrix = []
    for k in range(numberRows):
        contingencyMatrix.append([])
    #Ciclo de construcción
    for i in range(numberRows):
        for j in range(numberCols):
            count = 0
            for r in range(N):
                if firstVariable[r] == RowClass[i]:
                    if secondVariable[r] == ColumnClass[j]:
                        count = count + 1
            contingencyMatrix[i].append(count)
    return contingencyMatrix

#Devuelve el número de filas de la tabla de contingencia
def number_of_rows(cMatrix):
    """Return the number of rows of a given matrix
    
    Atributes
       cMatrix
       
    return number of rows
    """
    return len(cMatrix)

#Devuelve el número de columnas de la tabla de contingencia
def number_of_columns(cMatrix):
    """Return the number of columns of a given matrix
    
    Atributes
       cMatrix
       
    return number of columns
    """
    return len(cMatrix[0])

#Devuelve la lista de la suma de las filas
def sum_of_cols_contingency_matrix(cMatrix):
    """Return the list with the sum of each columns of a given matrix
    
    Atributes
       cMatrix
       
    return sum of columns of contingency matrix
    """
    sumOfColsCM = []
    rows_N = number_of_rows(cMatrix)
    columns_N = number_of_columns(cMatrix)
    for j in range(columns_N):
        suma = 0
        for i in range(rows_N):
            suma = suma + cMatrix[i][j]
        sumOfColsCM.append(suma)
    return sumOfColsCM

#Devuelve la lista de la suma de las columnas
def sum_of_rows_contingency_matrix(cMatrix):
    """Return the list with the sum of each rows of a given matrix
    
    Atributes
       cMatrix
       
    return sum of rows of contingency matrix
    """
    rows_N = number_of_rows(cMatrix)
    columns_N = number_of_columns(cMatrix)
    sumOfRowsCM = []
    for i in range(rows_N):
        suma = 0
        for j in range(columns_N):
            suma = suma + cMatrix[i][j]
        sumOfRowsCM.append(suma)
    return sumOfRowsCM

#Devuelve el valor N de una tabla de contingencia
def value_N_of_contingency_matrix(contMatrix):
    """Return the sum of each value of a given matrix
    
    Atributes
       cMatrix
       
    return sum of each value of contingency matrix
    """
    sumOfColumnsCM = sum_of_cols_contingency_matrix(contMatrix)
    suma = 0
    for i in range(len(sumOfColumnsCM)):
        suma = suma + sumOfColumnsCM[i]
    return suma

#Devuelve la matriz chi cuadrada de dos variables
def square_chi_index_cmatrix(firstV, secondV):
    """Return the square chi index between two list of qualitative
    variables
    
    Atributes
       firstV --list of values of first qualitative variable
       secondV --list of values of second qualitative variable
       
    return square chi index
    """
    CMatrix = contingency_frequency_matrix(firstV, secondV)
    return square_chi_idx_cmatrix(CMatrix)

#Devuelve la matriz chi cuadrada de una tabla de contingencia
def square_chi_idx_cmatrix(cMatrix):
    """Return the square chi index of a contingency matrix
    
    Atributes
       firstV --list of values of first qualitative variable
       secondV --list of values of second qualitative variable
       
    return square chi index
    """
    Rows = number_of_rows(cMatrix)
    Columns = number_of_columns(cMatrix)
    SquareCMatrix = []
    for k in range(Rows):
        SquareCMatrix.append([])
    SCj = sum_of_cols_contingency_matrix(cMatrix)
    SFi = sum_of_rows_contingency_matrix(cMatrix)
    for i in range(Rows):
        for j in range(Columns):
            squareCij = ds.square_number(cMatrix[i][j])
            Iij = float(squareCij) / (SCj[j] * SFi[i])
            SquareCMatrix[i].append(Iij)
    return SquareCMatrix

#Devuelve el valor Chi cuadrado de dos variables
def square_chi_index_contingency_v(firstV, secondV):
    """Return the square chi index of two list of qualitative variable
    
    Atributes
       firstV --list of values of first qualitative variable
       secondV --list of values of second qualitative variable
       
    return square chi index
    """
    CMatrix = contingency_frequency_matrix(firstV, secondV)
    return square_chi_index_contingency(CMatrix)

#Devuelve el índice chi-cuadrado de una tabla de contingencia
def square_chi_index_contingency(cMatrix):
    """Return the square chi index of a contingency matrix
    
    Atributes
       cMatrix
       
    return square chi index
    """
    sumOfIndexes = 0.0
    N_Value = value_N_of_contingency_matrix(cMatrix)
    squareChiIndexCM = square_chi_idx_cmatrix(cMatrix)
    rows = number_of_rows(cMatrix)
    columns = number_of_columns(cMatrix)
    for i in range(rows):
        for j in range(columns):
            sumOfIndexes = sumOfIndexes + squareChiIndexCM[i][j]
    return sumOfIndexes * N_Value - N_Value

#Devuelve el coeficiente de Pearson de dos conjuntos de variables
def pearson_coefficient_of_contingency_matrix(firstV, secondV):
    """Return the pearson coefficient for two sets of quatitative
    variables
    
    Atributes
       firstV --list of values of first qualitative variable
       secondV --list of values of second qualitative variable
       
    return pearson coefficient
    
    """
    CMatrix = contingency_frequency_matrix(firstV, secondV)
    return pearson_coefficient_of_cmatrix(CMatrix)

#Devuelve el coeficiente de Pearson con la matriz de contingencia
def pearson_coefficient_of_cmatrix(cMatrix):
    """Return the pearson coefficient for a contingency matrix
    variables
    
    Atributes
       cMatrix
       
    return pearson coefficient
    
    """
    CMatrix = cMatrix
    squareChiIndex = square_chi_index_contingency(CMatrix)
    N_Value = value_N_of_contingency_matrix(CMatrix)
    return float(squareChiIndex) / N_Value

#Devuelve el coeficiente de Pearson con N
def pearson_coefficient_value_N(squareChiIndex, N_Value):
    """Return the pearson coefficient from square Chi index and N
    
    Atributes
       cMatrix
       
    return pearson coefficient
    
    """
    return float(squareChiIndex) / N_Value

#Devuelve el coeficiente de Chuprov de dos conjuntos de variables
def chuprov_coefficient_contingency(firstV, secondV):
    """Return the chuprov coefficient for two sets of qualitative variable
    
    Atributes
       firstV --list of values of first qualitative variable
       secondV --list of values of second qualitative variable
       
    return chuprov coefficient
    
    """
    pearsonValue = pearson_coefficient_of_contingency_matrix(firstV, secondV)
    rows_M = len(qualitative_classes(firstV))
    columns_K = len(qualitative_classes(secondV))
    return pearsonValue / ((rows_M - 1) * (columns_K - 1))

#Devuelve el coeficiente de Chuprov de una tabla de contingencia
def chuprov_coefficient_cmatrix(cMatrix):
    """Return the chuprov coefficient for a contingency matrix
    
    Atributes
       cMatrix
       
    return chuprov coefficient
    
    """
    CMatrix = cMatrix
    pearsonValue = pearson_coefficient_of_cmatrix(CMatrix)
    rows_M = number_of_rows(CMatrix)
    columns_K = number_of_columns(CMatrix)
    return pearsonValue / ((rows_M - 1) * (columns_K - 1))

#Devuelve el coeficiente de Chuprov con M,K grados de libertad
def chuprov_coefficient_MK(pearsonValue, rows_M, columns_K):
    """Return the chuprov coefficient for m rows and k columns
    
    Atributes
       pearson coefficient value
       number of rows
       number of columns
       
    return chuprov coefficient
    
    """
    return pearsonValue / ((rows_M - 1) * (columns_K - 1))

#Devuelve el coeficiente de independencia
def independence_correlation_index(quantitativeV, qualitativeV):
    """Return the independence correlation index for two set of qualitative
    variables.
    
    Atributes
       pearson coefficient value
       number of rows
       number of columns
       
    return chuprov coefficient
    
    """
    N = len(quantitativeV)
    varianceX = ds.variance_value_sigma(quantitativeV)
    #Arreglos auxiliares
    weightedMeans = []
    weightList = []
    categoriesList = qualitative_classes(qualitativeV)
    #Cálculo de suma de valores y pesos
    for i in range(len(categoriesList)):
        count = 0
        sumValues = 0
        for j in range(N):
            if qualitativeV[j] == categoriesList[i]:
                count = count + 1
                sumValues = sumValues + quantitativeV[j]
        pi = float(count) / N
        weightList.append(pi)
        weightedMeans.append(float(sumValues) / count)
    varianceM = ds.weighted_variance(weightedMeans, weightList)
    return varianceM / varianceX

#llamada interna
if __name__ == '__main__':
    print("You should import this one in your main project")
