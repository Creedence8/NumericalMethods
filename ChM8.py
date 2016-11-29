
# coding: utf-8

# In[2]:

#Решение обыкновенного дифференциального уравнения

from math import *
from matplotlib import pylab as pl
import numpy as np

get_ipython().magic(u'matplotlib inline')

a = input(u'Значение a: ')

dx = 0.1
F = []

def dob(x,dx):
    z1=cos(x)**2 / cos(x)**3
    z2=cos(x+dx)**2 / cos(x+dx)**3
    z3=cos(x+2*dx)**2 / cos(x+2*dx)**3
    return (z3 - 2*z2 + z1) / dx**2 


x = np.arange(0, pi*2 , 0.1)
for x in x:
    y = round(a*exp(sqrt(abs(cos(x))**3)) + a*exp(-sqrt(abs(cos(x))**3)), 1)
zzz=cos(1)**2 / cos(1)**3 
l = pi/2 - 0.5
zz = [cos(z)**2 / cos(z)**3 for z in np.arange(0,l,0.01)]
pl.plot(np.arange(0,l,0.01), zz, color = 'red')
pl.show()
print zzz, dob(1, 0.0001)


# In[1]:

from math import *
from matplotlib import pylab as pl
import numpy as np

get_ipython().magic(u'matplotlib inline')

z = input(u'Значение a: ')

h = 0.1
a = 0
b =2*pi
n =  int((b-a)/h)
y = range(n+1)
c = range(n+1)
d = range(n+1)
y[0] = 1
y[n] = 1
m1=-(2-((cos(h)**3) * (h**2)))
n1=1
f1=cos(h)**2
c[1]=1/m1
d[1]=f1*(h**2)-n1*y[0]

for i in range(2,n):
    c[i]=1/(-(2-(cos(i*h)**3) * (h**2))-c[i-1])
    d[i]=(cos(i*h)**2)*(h**2) - c[i-1]*d[i-1]
for i in range(n-1,0,-1):
    y[i]=c[i]*(d[i]-y[i+1])

res = int(z/h)
print y[res]
pl.plot(np.arange(a,b,h), y, color = 'red')
pl.show()


# In[11]:

from math import *
from matplotlib import pylab as pl
import numpy as np

get_ipython().magic(u'matplotlib inline')

z = input(u'Значение a: ')

def alpha(x):
    return (cos(x))**3

def beta(x):
    return (cos(x))**2

nmax = 4000
dx = 2.*pi/nmax
ddx = 1./dx**2     
d = range(nmax)
col_beta = range(nmax)
rcol = range(nmax)
    
for i in range(nmax):
    d[i] = -2.*ddx+alpha(np.float64(i)*dx)
    col_beta[i]= beta(np.float64(i)*dx)
    rcol[i] = 0.
    
rcol[0]=ddx
rcol[nmax-2]=ddx
tochka=d[nmax-1]

for i in  range(nmax-1):
    mnoj=ddx/d[i]
    d[i+1]=d[i+1]-mnoj*ddx
    rcol[i+1] = rcol[i+1]-mnoj*rcol[i]
    col_beta[i+1] = col_beta[i+1]-mnoj*col_beta[i]

d[nmax-1] = tochka-mnoj*rcol[nmax-2]

for i in range(nmax-3,-1,-1):
    mnoj=ddx/d[i+1]
    rcol[i]=rcol[i]-rcol[i+1]*mnoj
    col_beta[i]=col_beta[i]-col_beta[i+1]*mnoj

mnoj=ddx/d[0]
d[nmax-1]=d[nmax-1]-mnoj*rcol[0]
col_beta[nmax-1]=col_beta[nmax-1]-mnoj*col_beta[0]

col_beta[nmax-1]=col_beta[nmax-1]/d[nmax-1]
tochka=col_beta[nmax-1]

for i in range(nmax-1):
    col_beta[i]=(col_beta[i]-rcol[i]*tochka)/d[i]

xi = z/dx

if xi<1.:
    n2=1.
    n1=nmax
else:
    n2=int(ceil(xi))
    n1=int(floor(xi))

k = (col_beta[n2]-col_beta[n1])/dx
b = col_beta[n1]-k*np.float(n1)*dx 
    
print round(k*z+b, 7)

p=np.arange(0,2*pi,dx)
y = [k*z+b for z in p]
#pl.plot(p, y)
#pl.show()     


# In[132]:

from math import *
import numpy as np
x =np.longdouble(20./3)
print x
print 20./3
print type(2**64)


# In[138]:

print 20./3


# In[43]:

from math import *
from matplotlib import pylab as pl
import numpy as np

get_ipython().magic(u'matplotlib inline')

z = input(u'Значение a: ')

def alpha(x):
    return (cos(x))**3

def beta(x):
    return (cos(x))**2

N = 4000
dx = 2.*pi/N
ddx = 1./dx**2     
d = range(N)
Cbeta = range(N)
RC = range(N)
    
for i in range(N):
    d[i] = -2.*ddx+alpha(np.float64(i)*dx)
    Cbeta[i]= beta(np.float64(i)*dx)
    RC[i] = 0.
    
RC[0]=ddx
RC[N-2]=ddx
ref=d[N-1]

for i in  range(N-1):
    mn=ddx/d[i]
    d[i+1]=d[i+1]-mn*ddx
    RC[i+1] = RC[i+1]-mn*RC[i]
    Cbeta[i+1] = Cbeta[i+1]-mn*Cbeta[i]

d[N-1] = ref-mn*RC[N-2]

for i in range(N-3,-1,-1):
    mn=ddx/d[i+1]
    RC[i]=RC[i]-RC[i+1]*mn
    Cbeta[i]=Cbeta[i]-Cbeta[i+1]*mn

mn=ddx/d[0]
d[N-1]=d[N-1]-mn*RC[0]
Cbeta[N-1]=Cbeta[N-1]-mn*Cbeta[0]

Cbeta[N-1]=Cbeta[N-1]/d[N-1]
ref=Cbeta[N-1]

for i in range(N-1):
    Cbeta[i]=(Cbeta[i]-RC[i]*ref)/d[i]

x = z/dx

if x == int(x):
    print Cbeta(x)
else:
    if x<1. or x >N-1:
        n2=1
        n1=int(N-1)
    else:
        n2=int(ceil(x))
        n1=int(floor(x))

k = (Cbeta[n2]-Cbeta[n1])/dx
b = Cbeta[n1]-k*np.float(n1)*dx 
    
print 'Значение f(a): ', round(k*z+b, 7)

j=np.arange(0,2*pi,dx)
y = [k*z+b for z in j]
p=np.arange(0,N,1)
y = [Cbeta[int(z)] for z in p]
pl.plot(j, y)
pl.show()     

