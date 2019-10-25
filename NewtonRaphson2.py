from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,acos
from math import sinh,cosh,tanh,asinh,acosh,atanh
import sympy
import math
from sympy import *
from matplotlib import pyplot
from math import e
from decimal import Decimal
from fractions import Fraction

h = sympy.symbols('h')
r = sympy.symbols('r')
l = sympy.symbols('l')
v = sympy.symbols('v')
sympy.init_printing(use_unicode=True)

print('Metodo de Newton Raphson\n')
ec=input('Ingrese la funcion a resolver: ')
#-8.5+(4*acos((2-x)/2)-(2-x*((4*x-(x**2))**(1/2))))*5
#-v+((r**2)*acos((r-h)/r)-(r-h*((2*r*h-(h**2))**(1/2))))*l
print ("Fx = ",ec)
ec2 = sympy.diff(ec,h)
ec2=str(ec2)
print ("F´x = ",ec2)
r=float(input('Ingrese el valor de R: '))
l=float(input('Ingrese el valor de L: '))
v=float(input(' Ingrese el valor de V: '))
h=float(input('Ingrese el valor de H: '))

def f(r,l,v,h):
    y=eval(ec)
    return y

def f2(r,l,v,h):
    return eval(ec2)

fh=f(r,l,v,h)
f1h=f2(r,l,v,h)
print ('f(',h,')= ',fh)
print ("f'(",h,')= ',f1h)