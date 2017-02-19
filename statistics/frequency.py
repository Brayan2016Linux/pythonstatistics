# -*- coding: utf-8 -*-
#!python
#frecuency.py

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
#*univariado, variables cuantitativas por medio de OOP  *
#*Desarrollado por Brayan Rodríguez                     *
#*Versión 1.2                                           *
#********************************************************

#Importa la libreria utilizando el nombre:
#if __name__ == '__main__':

#Para importar la librería
import statistics
import math

#Default precision:
precision = 2

#configuración de la precisión
def setPrecision(myprecision):
    precision = myprecision

#Devuelve el valor de la precisión
def getPrecision():
    return precision

#Devuelve el valor del límite de seguridad
def asuranceLimitValue():
    mypower = 5 * math.pow(10, - (getPrecision() + 1))
    return mypower

#Devuelve el tamaño total de la lista
def totalNumberOfValues(myList):
    return len(myList)

#Devuelve valor mínimo
def XminValue(myList):
    return myList[0]

#Devuelve el valor máximo
def XmaxValue(myList):
    return myList[len(myList) - 1]

#Devuelve la amplitud o recorrido de los datos
def dataRange(myList):
    return XmaxValue(myList) - XminValue(myList)

#Devuelve la amplitud de las clases
def classRange(myList, classNumber):
    myNumber = dataRange(myList) / float(classNumber)
    setPrecision = "{0:0." + str(getPrecision() - 1) + "f}"
    myString = ""
    myString = setPrecision.format(myNumber) + "5"
    return float(myString)

#Devuelve el límite inferior de una clase
def inferiorLimitClass(myList, classNumber):
    firstValue = XminValue(myList)
    classRangeValue = classRange(myList, classNumber)
    addValue = firstValue - asuranceLimitValue()
    setPrecision = "{0:0." + str(getPrecision()) + "f}"
    myLimitsList = []
    for i in range(classNumber):
        myLimitsList.append(float(setPrecision.format(addValue)))
        addValue = addValue + classRangeValue
    return myLimitsList

#Devuelve el límite superior de una clase
def superiorLimitClass(myList, classNumber):
    firstValue = XminValue(myList)
    classRangeValue = classRange(myList, classNumber)
    addValue = firstValue + classRangeValue - asuranceLimitValue()
    setPrecision = "{0:0." + str(getPrecision()) + "f}"
    myLimitsList = []
    for i in range(classNumber):
        myLimitsList.append(float(setPrecision.format(addValue)))
        addValue = addValue + classRangeValue
    return myLimitsList

#Devuelve la frequencia de la clase
def quantitativeFrequency(myList, classNumber):
    linfC = inferiorLimitClass(myList, classNumber)
    lsupC = superiorLimitClass(myList, classNumber)
    #Lista a devolver
    frequency = []
    #Primer ciclo
    for i in range(classNumber):
        infLimit = linfC[i]
        supLimit = lsupC[i]
        count = 0
        #Segundo ciclo
        for j in range(len(myList)):
            if myList[j] >= infLimit:
                if myList[j] < supLimit:
                    count = count + 1
        frequency.append(count)
    #Return
    return frequency

#Devuelve la clasificación de las variables cualitativas
def qualitativeClass(myList):
    classList = []
    addValue = ""
    comprobator = True
    for i in range(len(myList)):
        addValue = myList[i]
        for j in range(len(classList)):
            if classList[j] == myList[i]:
                comprobator = False
                break
            else:
                comprobator = True
        if comprobator is True:
            classList.append(addValue)
    return classList

#Devuelve la frecuencia de las variables
def qualitativeFrequency(myList):
    classList = qualitativeClass(myList)
    freqList = []
    for i in range(len(classList)):
        freqList.append(myList.count(classList[i]))
    return freqList

#Devuelve la matriz de contingencias
def contingencyMatrixFrequency(firstVariable, secondVariable):
    #Total de observaciones
    N = len(firstVariable)
    #Clasificación
    RowClass = qualitativeClass(firstVariable)
    ColumnClass = qualitativeClass(secondVariable)
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
def numberOfRows(cMatrix):
    return len(cMatrix)

#Devuelve el número de columnas de la tabla de contingencia
def numberOfColumns(cMatrix):
    return len(cMatrix[0])

#Devuelve la lista de la suma de las filas
def sumOfColsContingencyMatrix(cMatrix):
    sumOfColsCM = []
    rows_N = numberOfRows(cMatrix)
    columns_N = numberOfColumns(cMatrix)
    for j in range(columns_N):
        suma = 0
        for i in range(rows_N):
            suma = suma + cMatrix[i][j]
        sumOfColsCM.append(suma)
    return sumOfColsCM

#Devuelve la lista de la suma de las columnas
def sumOfRowsContingencyMatrix(cMatrix):
    rows_N = numberOfRows(cMatrix)
    columns_N = numberOfColumns(cMatrix)
    sumOfRowsCM = []
    for i in range(rows_N):
        suma = 0
        for j in range(columns_N):
            suma = suma + cMatrix[i][j]
        sumOfRowsCM.append(suma)
    return sumOfRowsCM

#Devuelve el valor N de una tabla de contingencia
def valueNOfContingencyMatrix(contMatrix):
    sumOfColumnsCM = sumOfColsContingencyMatrix(contMatrix)
    suma = 0
    for i in range(len(sumOfColumnsCM)):
        suma = suma + sumOfColumnsCM[i]
    return suma

#Devuelve la matriz chi cuadrada de dos variables
def squareChiIndexCMatrix(firstV, secondV):
    CMatrix = contingencyMatrixFrequency(firstV, secondV)
    return squareChiICMatrix(CMatrix)

#Devuelve la matriz chi cuadrada de una tabla de contingencia
def squareChiICMatrix(cMatrix):
    Rows = numberOfRows(cMatrix)
    Columns = numberOfColumns(cMatrix)
    SquareCMatrix = []
    for k in range(Rows):
        SquareCMatrix.append([])
    SCj = sumOfColsContingencyMatrix(cMatrix)
    SFi = sumOfRowsContingencyMatrix(cMatrix)
    for i in range(Rows):
        for j in range(Columns):
            squareCij = statistics.squareNumber(cMatrix[i][j])
            Iij = float(squareCij) / (SCj[j] * SFi[i])
            SquareCMatrix[i].append(Iij)
    return SquareCMatrix

#Devuelve el valor Chi cuadrado de dos variables
def squareChiIndexContingencyV(firstV, secondV):
    CMatrix = contingencyMatrixFrequency(firstV, secondV)
    return squareChiIndexContingency(CMatrix)

#Devuelve el índice chi-cuadrado de una tabla de contingencia
def squareChiIndexContingency(cMatrix):
    sumOfIndexes = 0.0
    N_Value = valueNOfContingencyMatrix(cMatrix)
    squareChiIndexCM = squareChiICMatrix(cMatrix)
    rows = numberOfRows(cMatrix)
    columns = numberOfColumns(cMatrix)
    for i in range(rows):
        for j in range(columns):
            sumOfIndexes = sumOfIndexes + squareChiIndexCM[i][j]
    return sumOfIndexes * N_Value - N_Value

#Devuelve el coeficiente de Pearson de dos conjuntos de variables
def pearsonCoefficientContingency(firstV, secondV):
    CMatrix = contingencyMatrixFrequency(firstV, secondV)
    return pearsonCoefficientOfCMatrix(CMatrix)

#Devuelve el coeficiente de Pearson con la matriz de contingencia
def pearsonCoefficientOfCMatrix(cMatrix):
    CMatrix = cMatrix
    squareChiIndex = squareChiIndexContingency(CMatrix)
    N_Value = valueNOfContingencyMatrix(CMatrix)
    return float(squareChiIndex) / N_Value

#Devuelve el coeficiente de Pearson con N
def pearsonCoefficientContValueN(squareChiIndex, N_Value):
    return float(squareChiIndex) / N_Value

#Devuelve el coeficiente de Chuprov de dos conjuntos de variables
def chuprovCoefficientContingency(firstV, secondV):
    pearsonValue = pearsonCoefficientContingency(firstV, secondV)
    rows_M = len(qualitativeClass(firstV))
    columns_K = len(qualitativeClass(secondV))
    return pearsonValue / ((rows_M - 1) * (columns_K - 1))

#Devuelve el coeficiente de Chuprov de una tabla de contingencia
def chuprovCoefficientCMatrix(cMatrix):
    CMatrix = cMatrix
    pearsonValue = pearsonCoefficientOfCMatrix(CMatrix)
    rows_M = numberOfRows(CMatrix)
    columns_K = numberOfColumns(CMatrix)
    return pearsonValue / ((rows_M - 1) * (columns_K - 1))

#Devuelve el coeficiente de Chuprov con M,K grados de libertad
def chuprovCoefficientMK(pearsonValue, rows_M, columns_K):
    return pearsonValue / ((rows_M - 1) * (columns_K - 1))

#Devuelve el coeficiente de independencia
def independenceCorrelationIndex(quantitativeV, qualitativeV):
    N = len(quantitativeV)
    varianceX = statistics.varianceValueSigma(quantitativeV)
    #Arreglos auxiliares
    weightedMeans = []
    weightList = []
    categoriesList = qualitativeClass(qualitativeV)
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
    varianceM = statistics.weightedVariance(weightedMeans, weightList)
    return varianceM / varianceX

#llamada interna
if __name__ == '__main__':
    print("You should import this one in your main project")
