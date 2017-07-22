# -*- coding: utf-8 -*-
<<<<<<< HEAD
"""
Created on Fri Jul 21 23:44:45 2017

@author: bradrd
"""

=======
#!python
#__init__.py

# para que sea ejecutable desde consola: $chmod 755 <nombre>.py
# agregar: #!/usr/bin/python
# para ejecutar: $./<nombre>.py

#importacion de valores
import statistics
import pearson
import frequency

#archivo de pruebas rescrito en Python 3

#Creación de la lista de pruebas nombrelista = [valor1, ..., valor n]
listaPruebas = [12.3, 13.3, 12.3, 14.3, 12.8, 15.3, 15.5, 16.2, 17.3, 17.3]
listaPesos = [12.0, 13.0, 12.0, 3.0, 20.0, 15.0, 5.0, 5.0, 10.0, 10.0]

i = 0

while i < 10:
    print("The value", i + 1, " is: ", listaPruebas[i: i + 1])
    i = i + 1


Suma = statistics.sumValueX(listaPruebas)
print("La suma de valores es: ", Suma)

Media = statistics.arithmeticMean(listaPruebas)
print("La media aritmética es:", Media)

SumaCuadrados = statistics.sumSquareValueX(listaPruebas)
print("La suma de los cuadrados es: ", SumaCuadrados)

desvEstandarSigma = statistics.standardDesviationSigma(listaPruebas)
print("La desviación estándar sigma es ", desvEstandarSigma)

desvEstandarNormal = statistics.standardDesviationNormal(listaPruebas)
print("La desviación estándar normal es ", desvEstandarNormal)

CVSigma = statistics.variationCoefficientSigma(listaPruebas)
print("El coeficiente de variacion sigma es ", CVSigma)

CVNormal = statistics.variationCoefficientNormal(listaPruebas)
print("El coeficiente de variacion normal es ", CVNormal)

varSigma = statistics.varianceValueSigma(listaPruebas)
print("La varianza sigma es ", varSigma)

varNormal = statistics.varianceValueNormal(listaPruebas)
print("La variancia normal es {0: .3f}".format(varNormal))


sumXY = pearson.sumValuesXY(listaPruebas, listaPesos)
pearsonXY = pearson.pearsonSigmaXY(listaPruebas, listaPesos)
covarXY = pearson.covarianceXY(listaPruebas, listaPesos)

print("La covariancia XY entre Prueba y Pesos {0:.3f} :".format(covarXY))
print("La suma XY entre Prueba y Pesos {0:.3f} :". format(sumXY))
print("El coeficiente pearson XY {0:.3f} :".format(pearsonXY))

weightedMean = statistics.weightedMean(listaPruebas, listaPesos)
print("Media ponderada {0: .3f}".format(weightedMean))

orderedList = statistics.orderedValues(listaPruebas)
print("Lista ordenada", orderedList)

quartileList = statistics.quartile(listaPruebas)
print("Cuartiles: 0% 25% 50% 75% 100%")
print(quartileList)

percentileR725 = statistics.percentileR7(listaPruebas, 75)
print("Percentil 75 R7: ", percentileR725)

percentileR825 = statistics.percentileR8(listaPruebas, 75)
print("Percentil 75 R8: ", percentileR825)

percentileR625 = statistics.percentileR6(listaPruebas, 75)
print("Percentil 75 R6: ", percentileR625)

listaSegunda = [1.0, 1.0, 1.5, 1.7, 2.0, 2.3, 2.4, 2.5, 2.6, 2.6,
2.6, 2.9, 3.0, 3.1, 3.4, 3.5, 3.5, 3.7, 4.0, 4.1, 4.1, 4.2, 4.5,
4.6, 5.0, 5.1, 5.3, 5.3, 5.4, 5.6, 5.8, 6.0, 6.4, 6.5, 6.5, 6.6,
6.7, 6.8, 6.9, 6.9, 7.0, 7.0, 7.1, 7.2, 7.2, 7.3, 7.3, 7.5, 7.5,
7.6, 7.6, 7.7, 7.8, 7.9, 8.0, 8.0, 8.1, 8.2, 8.2, 8.3, 8.3, 8.4,
8.6, 8.7, 8.9, 9.0]


numeroclases = 6
frequency.setPrecision(2)
listaValoresLI = frequency.inferiorLimitClass(listaSegunda, numeroclases)
listaValoresLS = frequency.superiorLimitClass(listaSegunda, numeroclases)
listaValoresFrec = frequency.quantitativeFrequency(listaSegunda, numeroclases)

ListaDistrib = [listaValoresLI, listaValoresLS, listaValoresFrec]
print("Frecuencias ", ListaDistrib)

listaTercera = ["1", "1", "1", "2", "2", "3", "3",
"3", "3", "2", "2", "3", "4", "2", "3", "3",
"4", "5", "5", "5", "3", "3", "2", "3", "3", "2",
"4", "4", "1", "1", "1", "1", "1", "1", "2", "2",
"2", "2", "2", "2", "1", "4", "3", "2", "2", "1",
"2", "1", "3", "2", "1", "1", "1", "1", "3", "3",
"3", "2", "4", "5", "5", "1", "1", "2", "2", "3"]


listaClase = frequency.qualitativeClass(listaTercera)
listaValFrec = frequency.qualitativeFrequency(listaTercera)
ListaDistrib2 = [listaClase, listaValFrec]
print("Frecuencias2 ", ListaDistrib2)

listaCuarta = ["NY", "NY", "CA", "FL", "FL", "LI", "LI",
"NM", "NM", "NM", "NM", "NM", "AL", "AL", "FL", "TX",
"NY", "NY", "FL", "FL", "MI", "TX", "TX", "AL", "TX", "TX",
"NM", "KT", "DW", "MI", "DW", "NY", "VG", "VG", "TX", "CA"]

listaClase2 = frequency.qualitativeClass(listaCuarta)
listaValFrec2 = frequency.qualitativeFrequency(listaCuarta)
ListaDistrib3 = [listaClase2, listaValFrec2]
print("Frecuencias3 ", ListaDistrib3)

myQuant1 = [267.0, 503.0, 208.0, 198.0, 250.0, 263.0,
    845.0, 471.0, 310.0, 830.0,
    759.0, 1200.0, 810.0, 650.0,
    1500.0, 1113.0, 2300.0, 900.0, 2100.0, 1621.0]

myQual1 = ["P", "P", "P", "P", "P", "P",
    "S", "S", "S", "S", "T", "T", "T", "T",
    "U", "U", "U", "U", "U", "U"]

coeffIndep = frequency.independenceCorrelationIndex(myQuant1, myQual1)
print("Coeficiente de independencia: ", coeffIndep)

CMatrix = [[200, 21, 2, 0], [217, 45, 5, 6], [156, 105, 46, 32],
    [73, 93, 24, 2], [6, 86, 52, 29]]

print("Numero filas: ", frequency.numberOfRows(CMatrix))
print("Numero columnas: ", frequency.numberOfColumns(CMatrix))

print("Valor de N ", frequency.valueNOfContingencyMatrix(CMatrix))


print("MatrixChiCuadContingencia ", frequency.squareChiICMatrix(CMatrix))


print("Indice Chi Cuadrado: ", frequency.squareChiIndexContingency(CMatrix))

print("Pearson Chi Cuadrado: ", frequency.pearsonCoefficientOfCMatrix(CMatrix))

print("Chuprov Chi Cuadrado: ", frequency.chuprovCoefficientCMatrix(CMatrix))

qualA = ["Masc", "Masc", "Fem", "Fem", "Fem", "Fem", "Masc", "Masc", "Fem"]

qualB = ["Ofic", "Obr", "Obr", "Art", "Art", "Ofic", "Art", "Ofic", "Art"]


frequency.setPrecision(3)

print("Indice Chi Cuadrado: ", frequency.squareChiIndexContingencyV(qualB, qualA))

print("Pearson: ", frequency.pearsonCoefficientContingency(qualB, qualA))

print("Chuprov: ", frequency.chuprovCoefficientContingency(qualB, qualA))

listaTercera = [1.0, 1.0, 1.5, 1.7, 2.0, 2.3, 2.4, 2.5, 2.6, 2.6,
2.6, 2.9, 3.0, 3.1, 3.4, 3.5, 3.5, 3.7, 4.0, 4.1, 4.1, 4.2, 4.5,
4.6, 5.0, 5.1, 5.3, 5.3, 5.4, 5.6, 5.8, 6.0, 6.4, 6.5, 6.5, 6.6,
6.7, 6.8, 6.9, 6.9, 7.0, 7.0, 7.1, 7.2, 7.2, 7.3, 7.3, 7.5, 7.5,
7.6, 7.6, 7.7, 7.8, 7.9, 8.0, 8.0, 8.1, 8.2, 8.2, 8.3, 8.3, 8.4,
8.6, 8.7, 8.9, 9.0]


listaCuarta = statistics.normalizedListTStudent(listaTercera)

print ("Lista no normalizada \n", listaTercera)
print("Media lista NO normalizada: {0: 0.3f}".format(statistics.arithmeticMean(listaTercera)))
print("Varianza lista NO normalizada: {0: 0.3f}".format(statistics.varianceValueNormal(listaTercera)))
print ("Lista Normalizada: \n", listaCuarta)
print("Media lista normalizada: {0: 0.3f}".format(statistics.arithmeticMean(listaCuarta)))
print ("Varianza lista normalizada: ", statistics.varianceValueNormal(listaCuarta))
print ("numero datos", frequency.totalNumberOfValues(listaTercera))
print ("Limites inferior", frequency.inferiorLimitClass(listaTercera, 6))
print ("Limites superior", frequency.superiorLimitClass(listaTercera, 6))
print ("Frecuencia lista Tercera:", frequency.quantitativeFrequency(listaTercera, 6))
print("Fin de pruebas")
>>>>>>> 495a74b7688f9f800789dd3256c1c09b3133fc97
