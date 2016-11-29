
# coding: utf-8

# In[1]:

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


# In[4]:

#Упорядочение элементов одномерного массива

N = input(u'Введите N: ')

iy = 5001.
mo = 65536
mn = 25137
mdb = 13849
ab = 65536

F = []
F.append(0)

def ran(iy):
    ran = iy/ab
    return ran

for i in xrange(100000):
    iy = (mn*iy+mdb) % mo
    F.append(ran(iy))
    
F1 = quicksort(F, 1, 100000)
F.sort()

print 'F[N]: ', round(F1[N], 7)

