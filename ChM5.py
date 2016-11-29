
# coding: utf-8

# In[3]:

#Поиск минимального и максимального элементов одномерного массива

from math import *

a = input(u'Значение a: ')

def func(N , a):
    return sin(N**(0.5*1.5)/log(N+a))

xmin = func(1 , a)
xmax = func(1 , a)

for N in xrange(1,100001):
    if func(N , a) < xmin:
        xmin = func(N , a)
        nmin = N
    if func(N , a) > xmax:
        xmax = func(N , a)
        nmax = N
print 'Nmin , Nmax: ', nmin,',', nmax

