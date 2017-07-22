# -*- coding: utf-8 -*-
#!python
#pearson.py
<<<<<<< HEAD
#Created: 07/21/2017
#Last Updated: 07/21/2017
=======
>>>>>>> 495a74b7688f9f800789dd3256c1c09b3133fc97

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
<<<<<<< HEAD
#*univariado, variables cuantitativas por medio de OOP  *
=======
#*univariado, variables cuantitativas                   *
>>>>>>> 495a74b7688f9f800789dd3256c1c09b3133fc97
#*Desarrollado por Brayan Rodríguez                     *
#*Versión 1.2                                           *
#********************************************************

#Importa la libreria utilizando el nombre:
#if __name__ == '__main__':

<<<<<<< HEAD
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
import sys
sys.path.append("./")
from statistics import descriptive_stat as stat

#Para trabajar con dos variables cuantitativas

#Devuelve la suma del producto de variables X y Y
def sum_of_values_XY(valuesX, valuesY):
    """Calculate sum of product two list of quatitative variables
    
    Atributes
        valuesX
        valuesY
        
    return sum of values XY
    """
    sumaXY = 0.0
    #for <iterador> in range(vi, vf, conteo)
    #for <iterator> in range(longitud)
    #for <iterator> in <lista>
    for i in range(len(valuesX)):
        sumaXY = sumaXY + valuesX[i - 1] * valuesY[i - 1]
    return sumaXY

#Devuelve la covarianza entre dos listas de variables X y Y
def covariance_XY(valuesX, valuesY):
    """Calculate covariance of two list of quatitative variables
    
    Atributes
        valuesX
        valuesY
        
    return number of row
    """
    arithMeanX = stat.arithmetic_mean(valuesX)
    arithMeanY = stat.arithmetic_mean(valuesY)
    sumValueXY = sum_of_values_XY(valuesX, valuesY)
    return sumValueXY / float(len(valuesX)) - (arithMeanX * arithMeanY)

#Devuelve el coeficiente de pearson sigma (n) de dos variables X y Y
def pearson_sigma_XY(valuesX, valuesY):
    """Calculate pearson sigma of two list of quatitative variables
    
    Atributes
        valuesX
        valuesY
        
    return pearson sigma (population)
    """
    desvStSigmaX = stat.standard_desviation_sigma(valuesX)
    desvStSigmaY = stat.standard_desviation_sigma(valuesY)
    covXY = covariance_XY(valuesX, valuesY)
    return covXY / (desvStSigmaX * desvStSigmaY)

#Devuelve el coeficiente de pearson normal (n-1) de dos variables X y Y
def pearson_normal_XY(valuesX, valuesY):
    """Calculate pearson normal of two list of quatitative variables
    
    Atributes
        valuesX
        valuesY
        
    return pearson normal (sample)
    """
    desvStNormalX = stat.standard_desviation_normal(valuesX)
    desvStNormalY = stat.standard_desviation_normal(valuesY)
    covNXY = covariance_XY(valuesX, valuesY)
    return covNXY / (desvStNormalX * desvStNormalY)


#llamada interna
if __name__ == '__main__':
    print("You should import this one in your main project")
=======
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
>>>>>>> 495a74b7688f9f800789dd3256c1c09b3133fc97
