# -*- coding: utf-8 -*-
#!python
#exception.py
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


#Manejo de Excepciones
#Definición de las excepciones de Vectores
class VectorError(Exception):
    """Define an exception when two vectors have different lenght"""
    pass

#Define las excepciones particulares dependientes
class DifferentVectorLenghtError(VectorError):
    """Define two different vector lenght error
    
    Atributes
        mensaje -- returning message
    """
    def __init__(self, message):
        self.message = message
        
#Definición de las excepciones de Matrices
class MatrixError(Exception):
    """Define an exception of different matrix"""
    pass

#Define la excepción de patrices particulares
class DifferentRowColumnError(MatrixError):
    """this exception is thrown when the number of column of A is
    different to rows of B
    
    Atributes
        mensaje -- returning message
    """
    def __init__(self, message):
        self.message = message