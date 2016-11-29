
# coding: utf-8

# In[7]:

from math import *

# n=7
a, n = input(u'Значения a , N: ')

def func(x, a):
    return log(x+1)*exp(-a*x)*(x**(-7./5))

def func0(x):
    return x**(-7./5)

x1 = 0.0000000000000001
margin = 0.00001
x2 = x1 + margin
i = 0
res = 0

while x2<n:
    i +=1
    if x1>1:
        margin = 1
    res += (x2-x1)*((func(x1, a)+func(x2, a)+4*func((x1+x2)/2,a))/6)
    x1 = x2
    x2 += margin
print 'Значение I: ', round(res, 4)

