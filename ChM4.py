
# coding: utf-8

# In[33]:

#Решение трансцендентного уравнения
from math import *
import numpy as np

i = open('I4.txt', 'r')
o = open('O4.txt', 'w')
A = []
for j in open('I4.txt', 'r'):
    A.append(int(j))

print A 
def func(x, a):
    return round((1.+a*x)**(-1), 6) != round (log(x), 6)

#Границы
x1 = 0.0000000000000001
x2 = 3

x= x1
for a in A:
    x1 = 0.0000000000000001
    x2 = 3

    x= x1
    while func(x, a):
        x = (x1 + x2)/2

        if (1.+a*x1)**(-1) > log(x1) and (1.+a*x)**(-1) > log(x):
            x1 = x 
        else:
            x2 = x
    o.write( str(a) + '  -   ' + str(x) +'\n')


# In[2]:

#Решение трансцендентного уравнения
from math import *

i = open('I4.txt')
o = open('O4.txt', 'w')
A = []
for j in range(2):
    A.append(int(i.readline()))

print A
def func(x, a):
    return round((1.+a*x)**(-1), 6) != round (log(x), 6)

#Границы
x1 = 0.0000000000000001
x2 = 3

x= x1
while func(x, 10):
    x = (x1 + x2)/2

    if (1.+10*x1)**(-1) > log(x1) and (1.+10*x)**(-1) > log(x):
        x1 = x 
    else:
        x2 = x
print x

