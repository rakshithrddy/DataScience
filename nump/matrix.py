from numpy import *

m1 = matrix('1 2 4; 1 4 6; 6 7 9')
m2 = matrix('1 6 4; 1 5 6; 6 2 9')
print(f'{m1}\n')

m3 = m1 + m2  # addition of 2 matrices

m4 = m1 * m2  # multiplication of 2 matrices

print(m3)
print('\n')
print(m4)