#!/bin/python3

def sqrt(n):
    if n==1: return 1
    b,e=0,n
    while True:
        m=(b+e)//2
        if m*m<=n:
            if (m+1)*(m+1)>n:
                return m
            else: b=m
        else: e=m


