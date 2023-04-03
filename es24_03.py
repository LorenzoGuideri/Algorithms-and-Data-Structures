#!/usr/bin/python3.10

from merge import sort

A=[3,4,2,5,6,1,7,8,9]

def Algo_x(A):
    i  =  1
    while  i < len(A):
        if  A[i] > A[i  +  1]:
            A[i],A[i  +  1]=A[i+1],A[i]
        p  =  i   
        q  =  i  +  1
        for  j in range(i  +  2,len(A)):
            if  A[j] < A[p]:
                p  =  j
            elif  A[j] > A[q]:
                q  =  j
        A[i],A[p]=A[p],A[i]
        A[i  +  1],A[q]=A[q],A[i+1]
        i  =  i  +  2
    return A

def Better_Algo_X(A):
    B=[A[0]]
    A=sort(A[1:])
    for i in range(len(A)//2):
        B.append(A[i])
        B.append(A[len(A)-i-1])
    return B

def partition_even_odd(A):
    i,j=0,len(A)-1
    while i<j:
        if A[i]%2:
            if not A[j]%2:
                A[j],A[i]=A[i],A[j]
                i+=1
            j-=1
        else:
            if A[j]%2:
                j-=1
            i+=1
    return A

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if not n%i: return False
    return True

def partition_primes_composites(A):
    i,j=0,len(A)-1
    while i<j:
        if not is_prime(A[i]):
            if is_prime(A[j]):
                A[j],A[i]=A[i],A[j]
                i+=1
            j-=1
        else:
            if not is_prime(A[j]):
                j-=1
            i+=1
    return A

def modulo_partition(A):
    for i in range(len(A)):
        ordered=True
        for j in range(len(A)-1):
            if A[j]%10>A[j+1]%10:
                A[j],A[j+1]=A[j+1],A[j]
                ordered=False
        if ordered:
            break
    return A

def three_way(A,v):
    p,q=1,1
    for i in A:
        if i<v:
            p+=1
        if i<=v:
            q+=1
    return p,q

def Sum_R(A,s,b,e):
    if b>e and s==0:
        return True
    elif b<=e and Sum_R(A,s,b+1,e):
        return True
    elif b<=e and Sum_R(A,s-A[b-1],b+1,e):
        return True
    else:
        return False

def Sum(A,s):
    return Sum_R(A,s,1,len(A))

'''
The algorithm computes for consequent numbers in array A that sum up to s. its complexity is O(n^2)
'''

def odd_in_odd(A):
    odds=0
    for i in A:
        if i%2:
            odds+=1
    menopari=odds>len(A)-odds
    massimo=2*(len(A)-odds) if menopari else 2*odds
    if menopari: i,j=0,1
    else: i,j=1,0
    while i<massimo:
        if A[i]%2 == menopari: #se ci sono meno pari e il numero è dispari OPPURE se ci sono meno dispari e il numero è pari 
            while A[j]%2 == menopari:
                j=j+2 if j<massimo else j+1
            A[i],A[j]=A[j],A[i]
        i+=2
    return A
    
        
        


# print(Algo_x(A))
# print(Better_Algo_X(A))
# print(partition_even_odd([7,  17,  74,  21, 11,  7,  9,  26,  10]))
# print(partition_primes_composites([7,  17,  74,  21, 11,  7,  9,  26,  10]))
# print(modulo_partition([7,  62,  5,  57,  12,  39,  5,  8,  16,  48]))
# print(three_way([1,2,3,4,5,6,7,7.6,7,1,2,4,8],7))
# print(Sum([3,4,6],10))
# print(odd_in_odd([50,  47,  92,  78,  76,  7,  60,  36,  59,  30,  50,  4]))
