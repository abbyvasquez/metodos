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
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

print('Metodo Interpolador de Newton\n')
Valor=([2,0.693147],[3,1.098612],[4,1.386294],[7,1.945910],[11,2.397875])

print (Valor)

b0=Valor[0][1]

print ("b 0 =",b0)
i=1
Valor2=([2,0.693147])
Valor3=([2,0.693147])
Valor4=([2,0.693147])
Valor3.append([3, 0.40546499999999996])
Valor4.append([3, 0.40546499999999996])
while i<=4:
           bi=(Valor[i][1]-Valor[i-1][1])/(Valor[i][0]-Valor[i-1][0])
           print ("b",i,"=",bi)
           Valor2.append([Valor[i][0],bi])
           i=i+1
           print (Valor2)

i=2
while i<=4:
           Valor2=([2, 0.693147], [3, 0.40546499999999996], [4, 0.287682], [7, 0.1865386666666667], [11, 0.11299124999999999])
           print (Valor2)
           bii=(Valor2[i][1]-(Valor2[i-1][1]))/(Valor2[i][0]-Valor2[i-2][0])
           print ("b",i,"=",bii)
           Valor3.append([Valor2[i][0],bii])
           i=i+1
i=3
while i<=4:
           Valor3=([2, 0.693147], [3, 0.405465], [4, -0.058892], [7, -0.025286], [11, -0.010506])
           print (Valor3)
           biii=(Valor3[i][1]-(Valor3[i-1][1]))/(Valor3[i][0]-Valor3[0][0])
           print ("b",i,"=",biii)
           Valor4.append([Valor2[i][0],bii])
           i=i+1

i=4
while i<=4:
           Valor4=([2, 0.693147], [3, 0.40546499999999996], [7, -0.010506773809523818], [11, -0.010506773809523818])
           print (Valor4)
           biiii=(Valor4[i][1]-(Valor4[i-1][1]))/(Valor4[i][0]-Valor4[0][0])
           print ("b",i,"=",biiii)
           i=i+1