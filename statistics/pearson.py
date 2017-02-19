# -*- coding: utf-8 -*-
#!python
#pearson.py

#/*******************************************************
#* Copyright (C) 2016-2017 Brayan Rodriguez D. <bradrd2009jp@gmail.com>
#* 
#* This file is part of Python Statistics.
#* 
#* Python Statistics can not be copied and/or distributed without the express
#* permission of Brayan Rodriguez and Imagine Cube Lab
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

#Para trabajar con dos variables cuantitativas

#Devuelve la covarianza entre dos listas de variables X y Y
def covarianceXY(valuesX, valuesY):
    arithMeanX = statistics.arithmeticMean(valuesX)
    arithMeanY = statistics.arithmeticMean(valuesY)
    sumValueXY = sumValuesXY(valuesX, valuesY)
    return sumValueXY / float(len(valuesX)) - (arithMeanX * arithMeanY)

#Devuelve el coeficiente de pearson sigma (n) de dos variables X y Y
def pearsonSigmaXY(valuesX, valuesY):
    desvStSigmaX = statistics.standardDesviationSigma(valuesX)
    desvStSigmaY = statistics.standardDesviationSigma(valuesY)
    covXY = covarianceXY(valuesX, valuesY)
    return covXY / (desvStSigmaX * desvStSigmaY)

#Devuelve el coeficiente de pearson sigma (n) de dos variables X y Y
def pearsonNormalXY(valuesX, valuesY):
    datosCovNXY = PearsonCoefficient()
    datosDesvStdNormal = Statistics()
    desvStNormalX = statistics.standardDesviationNormal(valuesX)
    desvStNormalY = statistics.standardDesviationNormal(valuesY)
    covNXY = covarianceXY(valuesX, valuesY)
    return covNXY / (desvStNormalX * desvStNormalY)

#Devuelve la suma del procto de variables X y Y
def sumValuesXY(valuesX, valuesY):
    sumaXY = 0.0
    #for <iterador> in range(vi, vf, conteo)
    #for <iterator> in range(longitud)
    #for <iterator> in <lista>
    for i in range(len(valuesX)):
        sumaXY = sumaXY + valuesX[i - 1] * valuesY[i - 1]
    return sumaXY

#llamada interna
if __name__ == '__main__':
    print("You should import this one in your main project")