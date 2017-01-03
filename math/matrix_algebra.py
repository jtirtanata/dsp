# Matrix Algebra

import numpy

A = numpy.matrix('1 3 3; 2 7 4')
B = numpy.matrix('1 -1; 0 1')
C = numpy.matrix('5 -1; 9 1; 6 0')
D = numpy.matrix('3 -2 -1; 1 2 3')
u = numpy.matrix('6 2 -3 5')
v = numpy.matrix('3 5 -1 4')
w = numpy.matrix('1; 8; 0; 5')

print('1. Matrix Dimensions')
print('1.1) A = {}'.format(str(A.shape)))
print('1.2) B = {}'.format(str(B.shape)))
print('1.3) C = {}'.format(str(C.shape)))
print('1.4) D = {}'.format(str(D.shape)))
print('1.5) u = {}'.format(str(u.shape)))
print('1.6) w = {}'.format(str(w.shape)))

print('2. Vector Operations')
print('2.1) u + v = {}'.format(numpy.add(u, v)))
print('2.2) u - v = {}'.format(numpy.subtract(u, v)))
print('2.3) αu = {}'.format(numpy.multiply(6, u)))
print('2.4) u·v = {}'.format(numpy.inner(u, v)))
print('2.5) ||u|| = {}'.format(numpy.linalg.norm(u)))

print('3. Matrix Operations')
print('3.1) A + C =')
try:
    print(numpy.add(A, C))
except ValueError:
    print('not defined')
print('3.2) A - Cᵀ =')
try:
    print(numpy.subtract(A, C.transpose()))
except ValueError:
    print('not defined')
print('3.3) Cᵀ + 3D =')
try:
    print(numpy.add(C.transpose(), numpy.multiply(3, D)))
except ValueError:
    print('not defined')
print('3.4) BA =')
try:
    print(numpy.matmul(B,A))
except ValueError:
    print('not defined')
print('3.5) BAᵀ =')
try:
    print(numpy.matmul(B, A.transpose()))
except ValueError:
    print('not defined')
