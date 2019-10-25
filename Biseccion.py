from sympy import *
from math import e
from numpy import log as ln

print('Metodo de Bisseccion\n')
ec=input('De la funcion a resolver: ')
x1=float(input('de el extremo inferior del intervalo aproximado: '))
x2=float(input('de el extremo superior del intervalo aproximado: '))
errordeseado=float(input('De el error deseado: '))


def f(x):
    return eval(ec)

while True:
    print("x1= ",x1," x2= ",x2)

    xmed=(x1+x2)/2
    print("ec",ec)
  #  print ("xmed",xmed)
    fxmed=f(xmed)
   # print ("fxmed",fxmed)
    if fxmed==0.0:
        break

    if (f(x1)*f(xmed))<0:
        x1=x1
        x2=xmed
    else:
        x1=xmed
        x2=x2

    error=abs(x2-x1)
    if error<errordeseado:
        break

print ('La raíz es',xmed)
input(' ')

#ln((x**2)+1)-e**(x/2)*cos(pi*x)