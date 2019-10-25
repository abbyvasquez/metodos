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

print('Metodo de Polinomio Interpolacion Lagrange\n')
Valor=([1,3],[2,-5],[3,-6],[4,2])
#L0x=((x-Valor[1][0])*(x-Valor[2][0])*(x-Valor[3][0]))/((Valor[0][0]-Valor[1][0])*(Valor[0][0]-Valor[2][0])*(Valor[0][0]-Valor[3][0]))

j=0
resultadoTotalizando=0
while (j<=3):
 resultado=0
 valorandonumerador=1
 valorandodivisor=1
 i=0
 while (i<=3):
            if (i!=j):
                     valorandonumerador=valorandonumerador*(x-Valor[i][0])
                     valorandodivisor=valorandodivisor*(Valor[j][0]-Valor[i][0])
            i=i+1
 resultado=valorandonumerador/valorandodivisor
 resultadoTot=(Valor[j][1])*resultado
 print ('L(',j,')=',resultado)
 resultadoTotalizando = resultadoTotalizando + resultadoTot
 j=j+1
 print ('F(',j-1,')=',resultadoTotalizando)

def f(x):
     return eval(resultadoTotalizando)

x=float(input('Ingrese el valor que desea reemplazar en la función: '))

resultadoTotalizando=str(resultadoTotalizando)
resultadoTotalizandoEvaluando = f(x)

print ('F(',j-1,')=',resultadoTotalizandoEvaluando)