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

print('Metodo de Polinomio Interpolacion Lagrange\n')
Valor=([1,0.1411],[1.2,-0.4425],[1.3,-0.6878],[1.5,-0.9775],[1.6,-0.9962],[1.9,-0.5507],[2,-0.2794],[2.2,0.3115])
#L0x=((x-Valor[1][0])*(x-Valor[2][0])*(x-Valor[3][0]))/((Valor[0][0]-Valor[1][0])*(Valor[0][0]-Valor[2][0])*(Valor[0][0]-Valor[3][0]))

j=0
resultadoTotalizando=0
while (j<=7):
 resultado=0
 valorandonumerador=1
 valorandodenominador=1
 i=0
 while (i<=7):
            if (i!=j):
                     valorandonumerador=valorandonumerador*(x-Valor[i][0])
                     valorandodenominador=valorandodenominador*(Valor[j][0]-Valor[i][0])
            i=i+1
 resultado=valorandonumerador/valorandodenominador
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

ec=(sin(3*1.78))

print ("El valor real, evaluado en la función original es = ",ec)

Err = abs(ec-resultadoTotalizandoEvaluando)
print ("Error relativo = ",Err)

Ead=Err/ec
print ("Error absoluto proporción = ",Err)
print ("Error absoluto porcentaje = ",abs(Ead*100), "%")

xx= (1,1.2,1.3,1.5,1.6,1.9,2,2.2)
yy= (0.1411,-0.4425,-0.6878,-0.9775,-0.9962,-0.5507,-0.2794,0.3115)
yy2= (0.1411000000000001,-0.44249999999999995,-0.6878000000000007,-0.9774999999999997,-0.9962,-0.5506999999999996,-0.27940000000000076,0.31150000000000067)
#yy2=

plt.title('Interpolación Lagrange')
plt.plot(xx,yy,'o', label = 'Lines')
plt.plot(xx,yy, label = 'Polinomio')
plt.plot(xx,yy2,'o', label = 'Lines')
plt.plot(xx,yy2, label = 'Polinomio')
plt.legend()
plt.show()