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

x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

print('Metodo Interpolador de Newton\n')
Valor=([2,0.693147],[3,1.098612],[4,1.386294],[7,1.945910],[11,2.397875])
#L0x=((x-Valor[1][0])*(x-Valor[2][0])*(x-Valor[3][0]))/((Valor[0][0]-Valor[1][0])*(Valor[0][0]-Valor[2][0])*(Valor[0][0]-Valor[3][0]))

print (Valor)

b0=Valor[0][1]

print (b0)

i=1
while i<=4:
           bi=(Valor[i][1]-Valor[i-1][1])/(Valor[i][0]-Valor[i-1][0])
           print (bi)
           i=i+1

