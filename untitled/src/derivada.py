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


print('Derivar\n')
ec=input('Ingrese la funcion a resolver: ') ##
ec2 = sympy.diff(ec,x)
ec2=str(ec2)
print (ec)
print (ec2)

