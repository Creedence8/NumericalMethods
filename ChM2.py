
# coding: utf-8

# In[19]:

from math import *

#область определения интеграла
a = 0
b = pi/2
#/область определения интеграла

c, n = input(u'значения c и N: ')

def func(x, c):
    return exp(c*sin(x))+sin(exp(c*x)/(x**2+1))

margin = a+(b-a)/n
b = a + margin
res = 0

for i in range(n):
    res += (b-a)*func((a+b)/2, c)
    a = b
    b += margin
    
print 'Значение I: ', round(res, 6)


# In[20]:

from math import *

#область определения интеграла
a = 0
b = pi/2
#/область определения интеграла

c, n = input(u'значения c и N: ')

def func(x, c):
    return exp(c*sin(x))+sin(exp(c*x)/(x**2+1))

margin = a+(b-a)/n
b = a + margin
res = 0

for i in range(n):
    res += (b-a)*((func(a, c)+func(b, c))/2)
    a = b
    b += margin
    
print 'Значение I: ', round(res, 6)


# In[24]:

from math import *

#область определения интеграла
a = 0
b = pi/2
#/область определения интеграла

c, n = input(u'значения c и N: ')

def func(x, c):
    return exp(c*sin(x))+sin(exp(c*x)/(x**2+1))

margin = a+(b-a)/n
b = a + margin
res = 0

for i in range(n):
    res += (b-a)*((func(a, c)+func(b, c)+4*func((a+b)/2,c))/6)
    a = b
    b += margin
    
print 'Значение I: ', round(res, 6)

