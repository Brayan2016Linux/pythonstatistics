# -*- coding: utf-8 -*-
#!python
#finanancial.py
#Financial Analysis
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

#devuelve el interés simple dada un principal y una tasa
def interest_value(PV, period, i):
    """Calculate simple interest of an amount in a n periods with
    a i interest
    
    Atributes
        PV --present value
        period
        i --interest rate
        
    return simple interest amount
    """
    return PV * i * period
    
#devuelve el descuento simple de una cantidad a futuro
def discount(FV, period, d):
    """Calculate simple discount of an amount in a n periods with
    a d discount
    
    Atributes
        FV --Future Value
        period
        d --discount rate
        
    return simple interest amount
    """
    return interest_value(FV, period, d)
    
#devuelve el valor futuro simple
def future_value(PV, period, i):
    """Calculate simple future value of an amount in a n periods with
    a i interest
    
    Atributes
        PV -- present value
        period
        i --interest rate
        
    return simple future value
    """
    return PV + interest_value(PV, period, i)
    
#devuelve el valor descontado a una tasa de descuento
def discount_value(FV, period, d):
    """Calculate simple discount value of an amount in a n periods with
    a i interest
    
    Atributes
        FV --future value
        period
        d --dicount rate
        
    return simple discount value
    """
    return FV - discount(FV, period, d)
    
#devuelve el valor presente simple
def present_value(FV, period, i):
    """Calculate simple present value of an FV in a n periods with
    a i interest
    
    Atributes
        FV --future value
        period
        i --interest rate
        
    return simple discount value
    """
    return FV / float(1 + i * period)
    
#devuelve el valor de descuento a una tasa de interes
def rational_discount_value(FV, period, i):
    """Calculate rational discount value of an FV in a n periods with
    a i interest
    
    Atributes
        FV --future value
        period
        i --interest rate
        
    return simple discount value
    """
    return FV - present_value(FV, period, i)
    
#devuelve la tasa de interés simple
def interest_rate(PV, FV, period):
    """Calculate simple interest rate of an FV in a n periods with
    a i interest
    
    Atributes
        PV --present value
        FV --future value
        period
        
    return i --interest rate
    """
    return (float(FV/PV) - 1) / float(period)

#llamada interna
if __name__ == '__main__':
    print("You should import this one in your main project")