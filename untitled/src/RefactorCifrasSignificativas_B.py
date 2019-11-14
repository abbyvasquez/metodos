import numpy

redondeo=int(input('Ingrese la cantidad de cifras a redondear: '))
def gaussJordan(matriz, vector):

    matrix = numpy.array(matriz, dtype=numpy.float64)
    vector = numpy.array(vector, dtype=numpy.float64)

    m = len(vector)
    x = numpy.zeros(m)

    for k in range(0, m):
        for r in range(k + 1, m):
            factor = (matrix[r, k] / matrix[k, k])

            vector[r] = vector[r] - (factor * vector[k])

            for c in range(0, m):
                matrix[r, c] = matrix[r, c] - (factor * matrix[k, c])


    x[m - 1] = (vector[m - 1] / matrix[m - 1, m - 1])

    for r in range(m - 2, -1, -1):
        suma = 0
        for c in range(0, m):
            suma = suma + matrix[r, c] * x[c]
        x[r] = (vector[r] - suma) / matrix[r, r]
    return x


A=[3, 2, 3], [2, -1, 0], [0, 3, 4]
B=[1, 2, 3]

#IF DE ORDENAMIENTO
if ((A[0][0]<A[1][0]) or (A[0][0]==A[1][0] and A[0][1]<A[1][1]) or (A[0][0]==A[1][0] and A[0][1]==A[1][1] and A[0][2]<A[1][2])):
    TEMP=A[0]
    TEMP2=B[0]
    A[0]=A[1]
    B[0]=B[1]
    A[1]=TEMP
    B[1]=TEMP2

if ((A[0][0]<A[2][0]) or (A[0][0]==A[2][0] and A[0][1]<A[2][1]) or (A[0][0]==A[2][0] and A[0][1]==A[2][1] and A[0][2]<A[2][2])):
    TEMP=A[0]
    TEMP2=B[0]
    A[0]=A[2]
    B[0]=B[2]
    A[2]=TEMP
    B[2]=TEMP2

if ((A[1][0]<A[2][0]) or (A[1][0]==A[2][0] and A[1][1]<A[2][1]) or (A[1][0]==A[2][0] and A[1][1]==A[2][1] and A[1][2]<A[2][2])):
    TEMP=A[1]
    TEMP2=B[1]
    A[1]=A[2]
    B[1]=B[2]
    A[2]=TEMP
    B[2]=TEMP2

print(A, ' Y ', B)

TODO=gaussJordan(A, B)
TODO2=gaussJordan(A, B)
if (redondeo==1):
    C = ['{:g}'.format(float(('{:.1g}').format(i))) for i in TODO]
else:
    if (redondeo==2):
        C = ['{:g}'.format(float(('{:.2g}').format(i))) for i in TODO]
    else:
        if(redondeo==3):
            C = ['{:g}'.format(float(('{:.3g}').format(i))) for i in TODO]
        else:
            if(redondeo==4):
                C = ['{:g}'.format(float(('{:.4g}').format(i))) for i in TODO]
            else:
                C = TODO

D=['{:g}'.format(float(('{:.10g}').format(i))) for i in TODO2]

print(C)
print(D)

