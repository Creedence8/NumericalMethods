
# coding: utf-8

# In[1]:

from math import *

beta = 1
a = complex(5, 3)
b = complex(14, beta)
c = complex(6, 8)

p = -(a**2)/3 + b
q = 2*(a**3)/27-a*b/3+c
Q = (p/3)**3 + (q/2)**2
A = (-q/2+Q**(1./2))**(1./3)
B = -p/(3*A)
Y = [A+B, -(A+B)/2+3**(1./2)*(A-B)/2j, -(A+B)/2-3**(1./2)*(A-B)/2j] 
X = [y - a/3 for y in Y]
res = [x**3+a*(x**2)+b*x+c for x in X]
print X
print res

