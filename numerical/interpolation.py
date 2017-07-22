# -*- coding: utf-8 -*-
#!python
#interpolation.py
#Numerical Analysis
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

#Para importar más de un módulo aledaño a nivel superior del py.
#import sys
#sys.path.append("./")
#from carpeta1 import <modulo> as <alias>
#from carpeta2 import <modulo> as <alias>

#importar librerías en subcarpetas al mismo nivel del .py
#from <carpeta> import <modulo> as <alias>

import math

#Epsilon de la máquina
def epsilon():
    """Calculate the epsilon --maximum error value-- of a machine
    
    Atributes
        
    return epsilon
    """
    epsilon = 1
    while True:
        if ( epsilon + 1 <= 1):
            break;
        else:
            epsilon = float(epsilon)/2
    epsilon = 2 * epsilon
    return epsilon
    
        
#Definición de la función
def f_value(x, coeff):
    """Calculate the value a polinomial function given a coefficient vector
    and x value
    
    Atributes
        
    return value of f
    """
    f = 0
    for i in range(len(coeff)):
        exponent = len(coeff) - (i + 1)
        f = f + coeff[i] * math.pow(x, exponent)
    return f
        
#Método de la bisección
def bisection(a, b, coeff, maxTolerance, iterations):
    """Calculate the value a x in a polinomial function 
    with given a coefficient vector when f(x) = 0
    
    Atributes
        
    return the bisection value
    """
    if(f_value(a, coeff)*f_value(b, coeff) < 0):
        count = 0
        for i in range(iterations):
            count = count + 1
            p = a + (b - a)/2
            if((f_value(p, coeff) == 0)or((b-a)/2 <= maxTolerance)):
                break;
            else:
                if(f_value(a, coeff)*f_value(p, coeff) > 0):
                    a = p
                else:
                    b = p
        if(count == iterations):
            return "Solution is not found"
        else:
            return p
    else:
        return "Values of f(a) and f(b) are with same sign"

#llamada interna
if __name__ == '__main__':
    print("You should import this one in your main project")