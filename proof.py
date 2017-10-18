# -*- coding: utf-8 -*-
#!python
#proof.py

#Para que funcione como un paquete, solo se escribe un archivo
#__init__.py no es necesario que contenga algo.

#Para importar librerías en carpetas aledañas a nivel superior del .py
#import sys
#sys.path.append("./<directorio>)
#import <modulo> as <alias>

#importar librerías en subcarpetas al mismo nivel del .py
#from <carpeta> import <modulo> as <alias>

# para que sea ejecutable desde consola: $chmod 755 <nombre>.py
# agregar: #!/usr/bin/python
# para ejecutar: $./<nombre>.py

#importacion de valores
from statistics import descriptive_stat as stat
from statistics import pearson
from statistics import frequency as freq
from vector import vector as vect
from matrix import matrix as mat
from statistics import pca
from financial import simple as fin
from numerical import interpolation as num


#archivo de pruebas rescrito en Python 3

#Creación de la lista de pruebas nombrelista = [valor1, ..., valor n]
listaPruebas = [12.3, 13.3, 12.3, 14.3, 12.8, 15.3, 15.5, 16.2, 17.3, 17.3]
listaPesos = [12.0, 13.0, 12.0, 3.0, 20.0, 15.0, 5.0, 5.0, 10.0, 10.0]

i = 0

while i < 10:
    print("The value", i + 1, " is: ", listaPruebas[i: i + 1])
    i = i + 1


Suma = stat.sum_of_values_X(listaPruebas)
print("La suma de valores es: ", Suma)

Media = stat.arithmetic_mean(listaPruebas)
print("La media aritmética es:", Media)

SumaCuadrados = stat.sum_of_square_values_X(listaPruebas)
print("La suma de los cuadrados es: ", SumaCuadrados)

desvEstandarSigma = stat.standard_desviation_sigma(listaPruebas)
print("La desviación estándar sigma es ", desvEstandarSigma)

desvEstandarNormal = stat.standard_desviation_normal(listaPruebas)
print("La desviación estándar normal es ", desvEstandarNormal)

CVSigma = stat.variation_coefficient_sigma(listaPruebas)
print("El coeficiente de variacion sigma es ", CVSigma)

CVNormal = stat.variation_coefficient_normal(listaPruebas)
print("El coeficiente de variacion normal es ", CVNormal)

varSigma = stat.variance_value_sigma(listaPruebas)
print("La varianza sigma es ", varSigma)

varNormal = stat.variance_value_normal(listaPruebas)
print("La variancia normal es {0: .3f}".format(varNormal))


sumXY = pearson.sum_of_values_XY(listaPruebas, listaPesos)
pearsonXY = pearson.pearson_sigma_XY(listaPruebas, listaPesos)
covarXY = pearson.covariance_XY(listaPruebas, listaPesos)

print("La covariancia XY entre Prueba y Pesos {0:.3f} :".format(covarXY))
print("La suma XY entre Prueba y Pesos {0:.3f} :". format(sumXY))
print("El coeficiente pearson XY {0:.3f} :".format(pearsonXY))

weightedMean = stat.weighted_mean(listaPruebas, listaPesos)
print("Media ponderada {0: .3f}".format(weightedMean))

orderedList = stat.ordered_values(listaPruebas)
print("Lista ordenada", orderedList)

quartileList = stat.quartile(listaPruebas)
print("Cuartiles: 0% 25% 50% 75% 100%")
print(quartileList)

percentileR725 = stat.percentileR7(listaPruebas, 75)
print("Percentil 75 R7: ", percentileR725)

percentileR825 = stat.percentileR8(listaPruebas, 75)
print("Percentil 75 R8: ", percentileR825)

percentileR625 = stat.percentileR6(listaPruebas, 75)
print("Percentil 75 R6: ", percentileR625)

listaSegunda = [1.0, 1.0, 1.5, 1.7, 2.0, 2.3, 2.4, 2.5, 2.6, 2.6,
2.6, 2.9, 3.0, 3.1, 3.4, 3.5, 3.5, 3.7, 4.0, 4.1, 4.1, 4.2, 4.5,
4.6, 5.0, 5.1, 5.3, 5.3, 5.4, 5.6, 5.8, 6.0, 6.4, 6.5, 6.5, 6.6,
6.7, 6.8, 6.9, 6.9, 7.0, 7.0, 7.1, 7.2, 7.2, 7.3, 7.3, 7.5, 7.5,
7.6, 7.6, 7.7, 7.8, 7.9, 8.0, 8.0, 8.1, 8.2, 8.2, 8.3, 8.3, 8.4,
8.6, 8.7, 8.9, 9.0]


numeroclases = 6
freq.set_precision(2)
listaValoresLI = freq.inferior_limit_class_value(listaSegunda, numeroclases)
listaValoresLS = freq.superior_limit_class_value(listaSegunda, numeroclases)
listaValoresFrec = freq.quantitative_frequency(listaSegunda, numeroclases)

ListaDistrib = [listaValoresLI, listaValoresLS, listaValoresFrec]
print("Frecuencias ", ListaDistrib)

listaTercera = ["1", "1", "1", "2", "2", "3", "3",
"3", "3", "2", "2", "3", "4", "2", "3", "3",
"4", "5", "5", "5", "3", "3", "2", "3", "3", "2",
"4", "4", "1", "1", "1", "1", "1", "1", "2", "2",
"2", "2", "2", "2", "1", "4", "3", "2", "2", "1",
"2", "1", "3", "2", "1", "1", "1", "1", "3", "3",
"3", "2", "4", "5", "5", "1", "1", "2", "2", "3"]


listaClase = freq.qualitative_classes(listaTercera)
listaValFrec = freq.qualitative_frequency(listaTercera)
ListaDistrib2 = [listaClase, listaValFrec]
print("Frecuencias2 ", ListaDistrib2)

listaCuarta = ["NY", "NY", "CA", "FL", "FL", "LI", "LI",
"NM", "NM", "NM", "NM", "NM", "AL", "AL", "FL", "TX",
"NY", "NY", "FL", "FL", "MI", "TX", "TX", "AL", "TX", "TX",
"NM", "KT", "DW", "MI", "DW", "NY", "VG", "VG", "TX", "CA"]

listaClase2 = freq.qualitative_classes(listaCuarta)
listaValFrec2 = freq.qualitative_frequency(listaCuarta)
ListaDistrib3 = [listaClase2, listaValFrec2]
print("Frecuencias3 ", ListaDistrib3)

myQuant1 = [267.0, 503.0, 208.0, 198.0, 250.0, 263.0,
    845.0, 471.0, 310.0, 830.0,
    759.0, 1200.0, 810.0, 650.0,
    1500.0, 1113.0, 2300.0, 900.0, 2100.0, 1621.0]

myQual1 = ["P", "P", "P", "P", "P", "P",
    "S", "S", "S", "S", "T", "T", "T", "T",
    "U", "U", "U", "U", "U", "U"]

coeffIndep = freq.independence_correlation_index(myQuant1, myQual1)
print("Coeficiente de independencia: ", coeffIndep)

CMatrix = [[200, 21, 2, 0], [217, 45, 5, 6], [156, 105, 46, 32],
    [73, 93, 24, 2], [6, 86, 52, 29]]

print("Numero filas: ", freq.number_of_rows(CMatrix))
print("Numero columnas: ", freq.number_of_columns(CMatrix))

print("Valor de N ", freq.value_N_of_contingency_matrix(CMatrix))


print("MatrixChiCuadContingencia ", freq.square_chi_idx_cmatrix(CMatrix))


print("Indice Chi Cuadrado: ", freq.square_chi_index_contingency(CMatrix))

print("Pearson Chi Cuadrado: ", freq.pearson_coefficient_of_cmatrix(CMatrix))

print("Chuprov Chi Cuadrado: ", freq.chuprov_coefficient_cmatrix(CMatrix))

qualA = ["Masc", "Masc", "Fem", "Fem", "Fem", "Fem", "Masc", "Masc", "Fem"]

qualB = ["Ofic", "Obr", "Obr", "Art", "Art", "Ofic", "Art", "Ofic", "Art"]


freq.set_precision(3)

print("Indice Chi Cuadrado: ", freq.square_chi_index_contingency_v(qualB, qualA))

print("Pearson: ", freq.pearson_coefficient_of_contingency_matrix(qualB, qualA))

print("Chuprov: ", freq.chuprov_coefficient_contingency(qualB, qualA))

listaTercera = [1.0, 1.0, 1.5, 1.7, 2.0, 2.3, 2.4, 2.5, 2.6, 2.6,
2.6, 2.9, 3.0, 3.1, 3.4, 3.5, 3.5, 3.7, 4.0, 4.1, 4.1, 4.2, 4.5,
4.6, 5.0, 5.1, 5.3, 5.3, 5.4, 5.6, 5.8, 6.0, 6.4, 6.5, 6.5, 6.6,
6.7, 6.8, 6.9, 6.9, 7.0, 7.0, 7.1, 7.2, 7.2, 7.3, 7.3, 7.5, 7.5,
7.6, 7.6, 7.7, 7.8, 7.9, 8.0, 8.0, 8.1, 8.2, 8.2, 8.3, 8.3, 8.4,
8.6, 8.7, 8.9, 9.0]


listaCuarta = stat.normalized_list_T_Student(listaTercera)

print ("Lista no normalizada \n", listaTercera)
print("Media lista NO normalizada: {0: 0.3f}".format(stat.arithmetic_mean(listaTercera)))
print("Varianza lista NO normalizada: {0: 0.3f}".format(stat.variance_value_normal(listaTercera)))
print ("Lista Normalizada: \n", listaCuarta)
print("Media lista normalizada: {0: 0.3f}".format(stat.arithmetic_mean(listaCuarta)))
print ("Varianza lista normalizada: ", stat.variance_value_normal(listaCuarta))
print ("numero datos", stat.number_of_values(listaTercera))
print ("Limites inferior", freq.inferior_limit_class_value(listaTercera, 6))
print ("Limites superior", freq.superior_limit_class_value(listaTercera, 6))
print ("Frecuencia lista Tercera:", freq.quantitative_frequency(listaTercera, 6))
print("Fin de pruebas")

vectX = [4, 3, 2]
vectY = [3, 1, 0]
try:
    print("Distancia es: {0:0.3f}".format(vect.distance(vectX, vectY)))
except TypeError:
    print('hola')
        
print("Producto Punto es: {0:0.3f}".format(vect.point_product(vectX, vectY)))
print("Modulo x: {0:0.3f}".format(vect.module(vectX)))
print("Modulo y: {0:0.3f}".format(vect.module(vectY)))
print("Angulo entre vectores es: {0:0.3f}".format(vect.angle(vectX, vectY)))

print("Vector Producto Cruz X x Y: ", vect.cross_product(vectX, vectY))
print("Vector unitario:", vect.unitary_vector(vectX))

Matrix = [[1, 2, 3], [3, 5, 4]]
print("Matrix is: ", Matrix)
print("Transpose of Matrix is:", mat.transpose(Matrix))
    
MatrixA = [[1, 2, 2],[2, 3, 2]]
MatrixB = [[6,0],[4,5], [2, 3]]
print("MatA * MatB: ", mat.product(MatrixA, MatrixB))
print("MatA * 3: ", mat.scalar_product(3, MatrixA))
print("MatA + MatB: ", mat.sum_of_matrix(MatrixA, mat.transpose(MatrixB)))
print("Mat - MatA: ", mat.substraction(Matrix, MatrixA))

Vector = [1,2,3,4]
MatrixC = [[1, 2, 2],[2, 3, 2]]
print("Diagonal: ", mat.diagonal(Vector))
print("Vector Diagonal: ", mat.diagonal_vector_of_matrix(mat.diagonal(Vector)))
print("Identity size 3", mat.identity(3))
print("RowVector: ", mat.row_vector(MatrixC, 1))

VectorM = [3,4,2,1]
VectorK = [4,5,6,7]
VectorW = [0.2, 0.3, 0.1, 0.4]
print("K: ", VectorM)
print("K: ", VectorK)
print("Addition M+K: ", vect.addition_vect(VectorM, VectorK))
print("Substraction M-K: ", vect.substraction_vect(VectorM, VectorK))
print("Distance(M,K)W: ", vect.distance_with_metric(VectorM, VectorK, VectorW))

matrixM = [[3,4,2,1],[4,5,6,7]]
print("Distance(M,K)W: ", mat.get_distance_between_rows(matrixM, VectorW, 0, 1))

TableAX = [[1,2,3,4],[4,5,6,7],[7,2,3,2],[3,2,1,4]]
TableAXCentred = pca.centralized_matrix(TableAX)
varianceMat =  pca.variance_matrix(TableAXCentred)
print("Covariance Matrix", varianceMat)
print("diagonalRSS: ", pca.diagonal_reciprocal_square_sigma(varianceMat))
print("diagonalRS: ", pca.diagonal_reciprocal_sigma(varianceMat))
print("Correlation matrix ", pca.correlation_r_matrix(varianceMat))

rate = 0.05/365
print("Intereses", fin.interest_value(2000, 50, rate))
print("VF", fin.future_value(2000, rate, 50))
print("PV", fin.present_value(fin.future_value(2000, 50, rate), 50, rate))
print("SimpleRate", fin.interest_rate(2000, 2013.70, 50)*365)

rate2 = 0.06/12
print("VF", fin.present_value(2500, 9, rate2))

rate3 = 0.08/12
print("DC", fin.discount_value(3080, 5, rate3))

rate4 = 0.06/12
print("Descuento racional", fin.rational_discount_value(1200, 1, rate4))

rateA = 0.05/360
discountA = fin.rational_discount_value(5000, 60, rateA)
print("Decuento RacionalA ", discountA)
rateB = 0.04/365
discountB = fin.rational_discount_value(5000, 60, rateB)
print("Decuento RacionalB ", discountB)
print("Ganancia ", discountA - discountB)

coeff = [1, -5, 6, 4]
print("f(p) = ", num.bisection(-1.5, 2.6, coeff, 0.0005, 15))
