#!/usr/bin/python3

def median_value(a=0,b=0,c=0):
    if a>b:
        if a<c: return a
        elif b>c: return b
        else: return c
    else:
        if a>c: return a
        elif b<c: return  b
        else: return c
    
def leap_year(n):
    if not n%400: return True
    elif not n%100: return False
    elif not n%4: return True
    else: return False
    
def classify_triangle(a,b,c):
    arr=[a,b,c]
    arr.sort()
    if arr[2]>=arr[0]+arr[1]: return "impossible"
    triangle=""
    if arr[2]**2>arr[1]**2+arr[0]**2: triangle+='obtuse '
    elif arr[2]**2==arr[1]**2+arr[0]**2:triangle+='right '
    else: triangle+='acute '     
    equals=0
    if arr[0]==arr[1]: equals+=1
    if arr[1]==arr[2]: equals+=1
    if equals==0: triangle+='scalene'
    elif equals==1: triangle +='isosceles'
    else: triangle+='equilateral'
    return triangle
