from math import sin, cos, tan, asin, acos, atan, sqrt, log, exp, acos
from math import sinh, cosh, tanh, asinh, acosh, atanh
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

A = [[3, 2, 3, 1],
     [2, -1, 0, 7 / 3],
     [0, 3, 4, 33 / 7]]

print("A =", A)

fila = 0
while j < 3:
    #   print (A[i][j])
    j = 0
    while fila < 3:
      #  if (i == j):
      #      print(A[i][j])
                if (A[fila][j] == A[0][0]):
                   print("aca", A[fila][j])
                j = j + 1
          #temp = j

    fila = fila + 1

# pivoteo parcial

# taller
##1. Probar la validez del procedimiento, redondeando con diferentes cifras decimales (pivoteo parcial) con matriz de 3*3
##el nos va a decir redondeelo a 4 muestreme el valor  |vt-ve|
##                                                     --------
##                                                     Vt

# matriz donde pueda ingresar 3 numeros de precision y redondee a 1 2 y 3 cifras
# y que saque el error procentual

# trabajo en parejas

# entrar matriz 3 * 3
# pal miercoles
