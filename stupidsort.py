#!/usr/bin/python3.10

def ssort(A):
    if len(A)<2: return A
    else:
        i=0
        for j in range(1,len(A)):
            if A[i]<A[j]:
                i=j
        A[-1],A[i]=A[i],A[-1]
        return ssort(A[:-1])+[A[-1]]

# print(ssort([1,2,3,4,5,6,0,5,7,1,-4,6]))
'''
Simple and inefficient way to sort a list recursively.
Works in O(n^2) and uses recursion.
It moves the biggest element to the end of the array and applies the algo again to A[:-1]
'''
