from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,acos
from math import sinh,cosh,tanh,asinh,acosh,atanh
import sympy
import math
from sympy import *
from matplotlib import pyplot
from math import e
from decimal import Decimal
from fractions import Fraction
import numpy as np
from array import array
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importamos math
from math import *

x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

#Definimos la funcion
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson38(n, a, b, f):
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, n):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x = a + i * h
        print("h= ",h)
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x, f)
    #sumamos los el primer elemento y el ultimo
    suma = suma + fx(a, f) + fx(b, f)
    #Multiplicamos por h/3
    rest = suma * (3*h / 8)
    #Retornamos el resultado
    return (rest)

#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

#valores de ejemplo para la funcion sin(x) con intervalos de
n = 2
a = 1
b = 2
f = 'x**3/(1+x**0.5)'

print("I =",simpson38(n, a, b, f))