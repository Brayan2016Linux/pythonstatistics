# -*- coding: utf-8 -*-
#!python
#matrix.py
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

#Para importar la librería
import math

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

import sys
sys.path.append("./")
from vector import vector as vect

#Cálculo de operaciones con Matrices

#Devuelve el número de filas una matriz
def number_of_rows(matrix):
    """Calculate the number of rows of a matrix
    
    Atributes
        matrix
        
    return number of row
    """
    return len(matrix)

#Devuelve el número de columnas de una matriz
def number_of_columns(matrix):
    """Calculate the number of column of a matrix
    
    Atributes
        matrix
        
    return number of row
    """
    return len(matrix[0])
    
#Devuelve la transpuesta de una matríz
def transpose(matrix):
    """Calculate the transpose matrix aij = bji
    
    Atributes
        matrix
        
    return number of row
    """
    Rows = number_of_columns(matrix)
    Columns = number_of_rows(matrix)
    #definición de matriz
    newMatrix = []
    #inicialización de matriz
    for k in range(Rows):
        newMatrix.append([])
    for i in range(Rows):
        for j in range(Columns):
            newentry = matrix[j][i]
            newMatrix[i].append(newentry)
    return newMatrix
    
#Producto entre matrices A[]nxm · B[]mxk  Rapidez: O(n^3)
def product(matrixA, matrixB):
    """Calculate product between two Matrix
    
    Atributes
        matrixA
        matrixB
        
    return matrix with the product
    """
    RowsA = number_of_rows(matrixA)
    ColumnsA = number_of_columns(matrixA)
    #Número de columnas de A = número de filas de B
    RowsB = number_of_rows(matrixB) 
    ColumnsB = number_of_columns(matrixB)
    if (ColumnsA == RowsB):
        #definición de matriz
        newMatrix = []
        #inicialización de matriz
        for k in range (RowsA):
            newMatrix.append([])
        #Multiplicación
        for i in range(RowsA):
            for j in range(ColumnsB):
                newMatrix[i].append(0)  #Equivalente a newMatrix[i][j] = 0
                for h in range(RowsB):
                    newMatrix[i][j] = newMatrix[i][j] + matrixA[i][h] * matrixB[h][j]
        return newMatrix
    else:
        print("This operation is not allowed")
        
#Cálculo del producto escalar
def scalar_product(scalar, matrix):
    """Calculate scalar product of a real number and a matrix cA
    
    Atributes
        scalar
        matrix
        
    return matrix with the product
    """
    newMatrix = matrix
    for i in range(number_of_rows(matrix)):
        for j in range(number_of_columns(matrix)):
            newMatrix[i][j] = scalar * newMatrix[i][j]
    return newMatrix
    
#Cálculo de la suma de dos matrices A[]nxm + B[]nxm
def sum_of_matrix(matrixA, matrixB):
    """Calculate sum between two Matrix
    
    Atributes
        matrixA
        matrixB
        
    return matrix with the sum
    """
    #Igual dimensión para ambas matrices
    RowsA = number_of_rows(matrixA)
    ColumnsA = number_of_columns(matrixA)
    #Número de columnas de A = número de filas de B
    RowsB = number_of_rows(matrixB) 
    ColumnsB = number_of_columns(matrixB)
    newMatrix = matrixA
    if ((RowsA == RowsB)&(ColumnsA == ColumnsB)):
        for i in range(RowsA):
            for j in range (ColumnsA):
                newMatrix[i][j] = newMatrix[i][j] + matrixB[i][j]
        return newMatrix
    else:
        print("This operation is not allowed")
    
#Cálculo de la resta de dos matrices A[]nxm - B[]nxm
def substraction(matrixA, matrixB):
    """Calculate substraction between two Matrix
    
    Atributes
        matrixA
        matrixB
        
    return matrix with the substraction
    """
    #Igual dimensión para ambas matrices
    RowsA = number_of_rows(matrixA)
    ColumnsA = number_of_columns(matrixA)
    #Número de columnas de A = número de filas de B
    RowsB = number_of_rows(matrixB) 
    ColumnsB = number_of_columns(matrixB)
    newMatrix = matrixA
    if ((RowsA == RowsB)&(ColumnsA == ColumnsB)):
        return sum_of_matrix(matrixA, scalar_product(-1, matrixB))
    else:
        print("This operation is not allowed")
        
#Cálculo de la traza de una matriz
#Suma de los elementos de la diagonal
def trace(matrix):
    """Calculate trace of a Matrix
    
    Atributes
        matrix
        
    return matrix with the substraction
    """
    #Solamente en la matrix cuadrada nxn
    Rows = number_of_rows(matrix)
    Columns = number_of_columns(matrix)
    if( Rows == Columns ):
        suma = 0
        for i in range(Rows):
            for j in range(Columns):
                if (i == j):
                    suma = suma + matrix[i][j]
        return suma
    else:
        print("This operation is not allowed")
    

#Matriz diagonal dado un vector
#Convierte un vectorX[]nx1 en una matriz diagonal D[]nxn
def diagonal(vector):
    """Calculate diagonal matrix from a vector
    
    Atributes
        vector
        
    return diagonal matrix
    """
    n = len(vector)
    #inicialización de la matriz diagonal
    diagonalMatrix = []
    for k in range(n):
        diagonalMatrix.append([])
    #construcción de la matriz diagonal 
    for i in range(n):
        for j in range(n):
            if(i == j):
                entry = vector[i]
                diagonalMatrix[i].append(entry)
            else:
                diagonalMatrix[i].append(0)
    return diagonalMatrix
    
#Extrae la diagonal de una Matriz Anxn
def diagonal_vector_of_matrix(matrix):
    """Calculate diagonal vector of a Matrix
    
    Atributes
        matrix
        
    return matrix with the substraction
    """
    diagonal = []
    Rows = number_of_rows(matrix)
    Columns = number_of_columns(matrix)
    for i in range(Rows):
        for j in range(Columns):
            if (i == j):
                diagonal.append(matrix[i][j])
    return diagonal
    
#Crea una matriz identidad de tamaño size
def identity(size):
    """Calculate a identity matrix from a given size
    
    Atributes
        matrix
        
    return identity matrix
    """
    diagonalVector = []
    for i in range(size):
        diagonalVector.append(1)
    return diagonal(diagonalVector)
    
#Obtener el vector fila en la posición n
def row_vector(matrix, position):
    """Calculate row of a Matrix in position n
    
    Atributes
        matrix
        position
        
    return row vector
    """
    rowvect = []
    columns = number_of_columns(matrix)
    for i in range(columns):
        rowvect.append(matrix[position - 1][i])
    return rowvect
    
#Obtener el vector fila en la posición n
def column_vector(matrix, position):
    """Calculate column of a Matrix in position n

    Atributes
        matrix
        position
        
    return column vector
    """
    columnvect = []
    rows = number_of_rows(matrix)
    for i in range(rows):
        columnvect.append(matrix[i][position - 1])
    return columnvect

#Para llamado de función externa    
if __name__ == '__main__':
    print("You should import this one in your main project")

    
    