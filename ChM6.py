
# coding: utf-8

# In[2]:

def eigh(F, v):
    X = np.eye(100,1)
    X [:,0]= v[0:100, 0]
    lamb = []
    i = 0 
    
    while True:
        X1 = np.dot(F,X)
        lamb.append (X1[0, 0] / X[0, 0])
        X = X1
        if i>0:
            if abs((lamb[i] - lamb[i-1])) < 0.1 or i>100:
                break
        i += 1
    return lamb[i]


# In[10]:

#Определение минимального собственного значения эрмитовой матрицы
#Метод итераций для нахождения собственных значений

from math import *
import numpy as np

a = input(u'Значение a: ')

#        if func(N , M , a) < Emin:
#            Emin = func(N , M , a)

def func(N , M , a):
    return sin((N+M)**(0.5*1.5)/log(N+M+a))

Emin = func(1 , 1 , a)
F = np.eye(100)

for N in xrange(1,101):
    for M in xrange(1,101):
#        F[N - 1 , M - 1] = func(N , M , a)
        if M  == N:
           F[N - 1 , M - 1] = M 

w, v = np.linalg.eigh(F)

print "Собственное значение:\n", round(eigh(F,v),5), '\n'

#print 'Emin: ', Emin


# In[160]:

from math import *
import numpy as np

def eigh(F, v):
    X = np.array([[1.], [1], [1]])
    lamb = []
    i = 0 
    
    while True:
        X1 = np.dot(F,X)
        lamb.append (X1[0, 0] / X[0, 0])
        X = X1
        if i>0:
            if abs((lamb[i] - lamb[i-1])) < 0.1 or i>400:
                break
        i += 1
    return lamb , i


F = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])
w, v = np.linalg.eigh(F)

print "Собственное число:\n", eigh(F,v), '\n', F, w


# In[188]:

F = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])
for i in range(3):
    if i % 2 != 0:
        F [i,0] = 0
print F


# In[9]:

#Определение минимального собственного значения эрмитовой матрицы
#Метод итераций для нахождения собственных значений

from math import *
import numpy as np

a = input(u'Значение a: ')

def func(N , M , a):
    return np.float64(sin((N+M)**(0.5*1.5)/log(N+M+a)))

F = np.eye(100)

for N in xrange(1,101):
    for M in xrange(1,101):
        F[N - 1 , M - 1] = func(N , M , a)
        
def eigh(F, v):
    X = np.eye(100,1)
    X [:,0]= v[0:100, 0]
    for i in range(100):
        if i % 10 == 0:
            X [i,0] = 1
            
    lamb2 = 0
    i = 0 
    
    while True:
        X1 = np.dot(F,X)
        lamb1 = lamb2
        lamb2 = (X1[0, 0] / X[0, 0])
        X = X1
        print lamb2
        if i>0:
            if abs(lamb2 - lamb1) < 1 or i>150:
                break
        i += 1
    return lamb2

w, v = np.linalg.eigh(F)

print "Собственное число:\n", w.min(), eigh(F, v)

