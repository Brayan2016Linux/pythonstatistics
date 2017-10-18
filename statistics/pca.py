# -*- coding: utf-8 -*-
#!python
#pca.py
#Principal Components Analysis
#Created: 07/21/2017
#Last Updated: 07/21/2017

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
from vector import vector as vect
from matrix import matrix as mat
from statistics import descriptive_stat as stat


#Calcula la métrica D de pesos weight para un tamaño size
def diagonal_metric_weight_matrix(size, weight):
    """Calculate diagonal metric weight matrix
    
    Atributes
        size
        weight
        
    return diagonal metric weigth matrix
    """
    identity = mat.identity(size)
    return mat.scalar_product(weight, identity)

#Calcula la matriz de varianza-covarianza V = transp(X) * D * X
def variance_matrix(CentralizedTableX):
    """Calculate variance of a centralized values matrix
    
    Atributes
        CentralizedTableX
        
    return variaces matrix
    """
    size = mat.number_of_rows(CentralizedTableX)
    weight = 1/float(size)
    transposeX = mat.transpose(CentralizedTableX)
    diagonal = diagonal_metric_weight_matrix(size, weight)
    return mat.product(transposeX, mat.product(diagonal, CentralizedTableX))
    
#Centralizar observaciones de una variable
def centralized_matrix(TableX):
    """Return a centralized values matrix
    
    Atributes
        TableX
        
    return centralized matrix
    """
    rows = mat.number_of_rows(TableX)
    columns = mat.number_of_columns(TableX)
    newMatrix = TableX
    for j in range(columns):
        partialVector = mat.column_vector(newMatrix, j + 1)
        ArithmeticMean = stat.arithmetic_mean(partialVector)
        for i in range(rows):
            newMatrix[i][j] = newMatrix[i][j] - ArithmeticMean
    return newMatrix

#Calcula métrica D 1/sigma^2
def diagonal_reciprocal_square_sigma(varianceMatrix):
    """Return a diagonal reciprocal square variances matrix
    
    Atributes
        varianceMatrix
        
    return a diagonalreciprocal square variances matrix
    """
    vectordiagonal = mat.diagonal_vector_of_matrix(varianceMatrix)
    reciprocalvec = vect.reciprocal(vectordiagonal)
    return mat.diagonal(reciprocalvec)

#Calcula métrica D 1/sigma
def diagonal_reciprocal_sigma(varianceMatrix):
    """Return a diagonal reciprocal variances matrix
    
    Atributes
        varianceMatrix
        
    return a diagonalreciprocal variances matrix
    """
    vectordiagonal = mat.diagonal_vector_of_matrix(varianceMatrix)
    #VectorSigma
    sigma = []
    #square root of vector
    for i in range(len(vectordiagonal)):
        sigma.append(math.sqrt(vectordiagonal[i]))
    reciprocalvec = vect.reciprocal(sigma)
    return mat.diagonal(reciprocalvec)
    
#Calcula la matríz de correlación D 1/sigma * R * D 1/sigma
def correlation_r_matrix(varianceMatrix):
    """Return a correlation R matrix
    
    Atributes
        varianceMatrix
        
    return a correlation R matrix
    """
    D = diagonal_reciprocal_sigma(varianceMatrix)
    return mat.product(D, mat.product(varianceMatrix, D))

#Para llamado de función externa    
if __name__ == '__main__':
    print("You should import this one in your main project")