#!/usr/bin/python3

def rht(A,n):
    elements={}
    final=list()
    for i in A:
        if i in elements:
            elements[i]+=1
        else:
            elements[i]=1
    for i in A:
        if elements[i]<=n:
            final.append(i)
    return final
# print(rht([1,2,3,4,4,4,4,4,5,5,5], 3))

def sort_evens_odds(A):
    A.sort()
    working = False
    for n in range(len(A)-1, 0, -1):
        for i in range(n):
            if A[i]%2 and not A[i + 1]%2:
                working = True
                A[i], A[i + 1] = A[i + 1], A[i]       
        if not working:
            break
    return A
 
#print(sort_evens_odds([1,2,3,4,5,6]))

def shittysort(A):
    working = False
    for n in range(len(A)-1, 0, -1):
        for i in range(n):
            if A[i] > A[i + 1]:
                working = True
                A[i], A[i + 1] = A[i + 1], A[i]       
        if not working:
            break
    return A

def mysort(A,n):
    A.shittysort(A)
    if n: return A
    return A[::-1]

#A = [1,10,45,100,5,293]
#print(shittysort(A))
