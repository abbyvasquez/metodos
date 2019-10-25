from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp
from math import sinh,cosh,tanh,asinh,acosh,atanh
import sympy
import math
from sympy import *
from matplotlib import pyplot
from math import e
from decimal import Decimal
from fractions import Fraction
from math import *

x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)


print('Metodo de punto fijo\n')
ec=input('Ingrese la funcion a resolver: ') ##
ec2 = sympy.diff(ec,x)
ec2=str(ec2)
print (ec)
print (ec2)

def g(x):
    y=eval(ec)
    return y

def g2(x):
    return eval(ec2)

x0=float(input('Ingrese el valor inicial X0: '))
n=float(input('Ingrese la cantidad de iteraciones: '))
i=0
Ea=1
#tol=0.41
n0=50
while true:
    #i<=n0:
    gx=g(x0)
    g1x=g2(x0)
    Ea = abs(gx-x0)

    if (abs(g1x)<1):
      comparacion="Si es < 1"
    else:
      comparacion="NO es < 1"
    print(" n =",i," Xn= ",x0,"g(Xn) =",gx, " Ea =", Ea, " g'(x) = ",g1x, " Comparación = ", comparacion)

   ## if abs(p-p0)<=tol:
    if i==(n-1):
        print("Fin punto fijo.")
        break
    i=i+1
    x0=gx
if i>n0:
    print("El metodo no converge ")