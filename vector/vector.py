# -*- coding: utf-8 -*-
#!python
#vector.py
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


#Para importar la librería matemáticas
import math

#Calcula la distancia entre dos vectores n dimensionales
def distance(vectorX, vectorY):
    """Calculate distance between two vectors"
    
    Atributes
        vectorX
        vectorY
        
    return distance
    """
    #vectores de igual longitud
    if(len(vectorX) == len(vectorY)):
        squaremodule = 0
        for i in range(len(vectorX)):
            difference = vectorX[i]-vectorY[i]
            squaredifference = difference * difference
            squaremodule = squaremodule + squaredifference
        return math.sqrt(squaremodule)
            
#Calcula el producto punto de los vectores
def point_product(vectorX, vectorY):
    """Calculate point product between two vectors"
    
    Atributes
        vectorX
        vectorY
        
    return point product
    """
    #vectores de igual longitud
    if(len(vectorX) == len(vectorY)):
        pointproduct = 0
        for i in range(len(vectorX)):
            product = vectorX[i] * vectorY[i]
            pointproduct = pointproduct + product
        return pointproduct
        
#Cálculo del producto cruz de dos vectores de dimensión 3
def cross_product(vectorX, vectorY):
    """Calculate cross product between two vectors"
    
    Atributes
        vectorX
        vectorY
        
    return cross product
    """
    #Solo aplica para vectores tridimensionales
    entry1 = vectorX[1] * vectorY[2] - vectorX[2] * vectorY[1]
    entry2 = -vectorX[0] * vectorY[2] + vectorX[2] * vectorY[0]
    entry3 = vectorX[0] * vectorY[1] - vectorX[1] * vectorY[0]
    newvector = [entry1,entry2,entry3] 
    return newvector

#Calcula el módulo de un vector
def module(vectorX):
    """Calculate module or length of a vector"
    
    Atributes
        vectorX
        
    return module
    """
    squaremodule = 0;
    for i in range(len(vectorX)):
        product = vectorX[i]*vectorX[i]
        squaremodule = squaremodule + product;
    return math.sqrt(squaremodule)    
    
#Cálculo del vector unitario en la misma dirección
def unitary_vector(vector):
    """Calculate the unitary vector from another"
    
    Atributes
        vector
        
    return unitary vector
    """
    Module = module(vector)
    newvector = vector
    for i in range(len(newvector)):
        newvector[i] = newvector[i] / Module
    return newvector

#Calcula el ángulo entre vectores en grados:
def angle(vectorX, vectorY):
    """Calculate angle between two vectors"
    
    Atributes
        vectorX
        vectorY
        
    return angle --degrees
    """
    #vectores de igual longitud
    if(len(vectorX) == len(vectorY)):
        PointProduct = point_product(vectorX, vectorY)
        moduleX = module(vectorX)
        moduleY = module(vectorY)
        return math.degrees(math.acos(PointProduct /(moduleX * moduleY)))
        
#Calcula el tamaño de un vector:
def size(vector):
    return len(vector)
    
#Calcula el recíproco de los elementos de un vector:
#Para cada a[i] devuelve 1/a[i]
def reciprocal(vector):
    """Calculate reciprocal vector 1/a of a given vector"
    
    Atributes
        vector
        
    return reciprocal vector
    """
    reciprocalvector = []
    for i in range(len(vector)):
        reciprocal = 1/float(vector[i])
        reciprocalvector.append(reciprocal)
    return reciprocalvector
        
#Calcula el vector luego de multiplicar por un escalar:
#Para cada a[i] * c devuelve c*a[i]
def scalar_vect(scalar, vector):
    """Calculate new vector given a vector and scalar"
    
    Atributes
        scalar
        vector
        
    return scalar_vect
    """
    scalarvector = []
    for i in range(len(vector)):
        result = scalar * float(vector[i])
        scalarvector.append(result)
    return scalarvector
    
#Calcula la suma de dos vectores:
#Para cada a[i] , b[i] devuelve a[i] + b[i]
def addition_vect(vectorA, vectorB):
    """Calculate new vector given a vector and scalar"
    
    Atributes
        vectorA
        vectorB
        
    return scalar_vect
    """
    additionvector = []
    for i in range(len(vectorA)):
        result = float(vectorA[i]) + float(vectorB[i]) 
        additionvector.append(result)
    return additionvector
    
#Calcula la resta de dos vectores:
#Para cada a[i] , b[i] devuelve a[i] - b[i]
def substraction_vect(vectorA, vectorB):
    """Calculate new vector given a vector and scalar"
    
    Atributes
        vectorA
        vectorB
        
    return scalar_vect
    """
    subvector = []
    for i in range(len(vectorA)):
        result = float(vectorA[i]) - float(vectorB[i]) 
        subvector.append(result)
    return subvector
    
#Calcula la distancia entre dos vectores bajo una métrica
def distance_with_metric(vectorX, vectorY, metric):
    """Calculate distance between two vectors under a metric"
    
    Atributes
        vectorX
        vectorY
        metric
        
    return distance_with_metric
    """
    #vectores de igual longitud
    if(len(vectorX) == len(vectorY)):
        squaremodule = 0
        for i in range(len(vectorX)):
            difference = vectorX[i]-vectorY[i]
            squaredifference = (difference ** 2) * metric[i]
            squaremodule = squaremodule + squaredifference
        return math.sqrt(squaremodule)
        
#La correlación de pearson puede verse como el cos(angle)
#Para llamado de función externa    
if __name__ == '__main__':
    print("You should import this one in your main project")
