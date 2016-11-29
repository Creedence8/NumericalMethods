
# coding: utf-8

# In[79]:

def sum(a):
    res = 0
    for k in xrange (2500):
        if k % 2 == 0:
            mn = 1.
        else:
            mn = -1.
        res += mn / ((2*k+1)**2+a)
    return round(res, 7) 
print sum(0.5)
def sum1(a):
    res = 0
    for k in xrange (2500, -1, -1):
        if k % 2 == 0:
            mn = 1.
        else:
            mn = -1.
        res += mn / ((2*k+1)**2+a)
    return round(res, 7) 
print sum1(0.5)


# In[2]:

from decimal import *
import numpy as np
getcontext().prec = 2
#print Decimal (11) / Decimal (3)


# In[3]:

20./3

