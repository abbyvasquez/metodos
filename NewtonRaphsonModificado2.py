from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,acos
from math import sinh,cosh,tanh,asinh,acosh,atanh
import sympy
import math
from sympy import *
from matplotlib import pyplot
from math import e
from decimal import Decimal
from fractions import Fraction

x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

print('Metodo de Newton Raphson modificado\n')
ec=input('Ingrese la funcion a resolver: ')
print ('Fx =',ec)
ec2 = sympy.diff(ec,x)
ec2=str(ec2)
print ('F´x =',ec2)
ec3 = sympy.diff(ec2,x)
ec3=str(ec3)
print ('F´´x =',ec3)

X0=float(input('Ingrese el valor inicial X0: '))
n=float(input('Ingrese la cantidad de iteraciones: '))

def f(x):
    y=eval(ec)
    return y

def f1(x):
    return eval(ec2)

def f2(x):
    return eval(ec3)

con=1
while True:
 dx=f(X0)
 dx1=f1(X0)
 dx2=f2(X0)

 print ('f(',X0,') = ',dx,'\n','f´(',X0,') =',dx1,'\n','f´´(',X0,') =',dx2)

 X1=X0-((dx1*dx)/((dx1**2)-(dx*dx2)))

 print ('X',con,'=',X1)
 X0=X1
 if (con==n):
     print ('fin')
     break
 con=con+1