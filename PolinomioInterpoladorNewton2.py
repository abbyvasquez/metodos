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

import numpy as np
import matplotlib.pyplot as plt

def coef(x, y):
    '''x : array of data points
       y : array of f(x)  '''
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = [2,3,4,7,11]
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a) # return an array of coefficient

def Eval(a, x, r):

    ''' a : array returned by function coef()
       x : array of data points
       r : the node to interpolate at  '''

x.astype(float)
n = len( a ) - 1
temp = a[n] + (r - x[n])
for i in range( n - 1, -1, -1 ):
    temp = temp * ( r - x[i] ) + a[i]
    return tem # return the y_value interpolation