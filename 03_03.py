#!/usr/bin/python3

def is_growing(a,b,c):
    maximo=a[b]
    for i in a[b:c+1]:
        if i<maximo: return False
        maximo=i
    return True
def isnt_growing(a,b,c):
    minimo=a[b]
    for i in a[b:c+1]:
        if i>minimo: return False
        minimo=i
    return True

def is_monotonic(a,b,c):
	return is_growing(a,b,c) or isnt_growing(a,b,c)

def longest_growing(a):
	lenght,maxlen,maximo =1,0,a[0]
	for i in a[1:]:
		if i>= maximo: lenght+=1
		else: lenght=1
		maximo=i
		if maxlen<lenght: maxlen=lenght
	return maxlen

def longest_notgrowing(a):
	lenght,maxlen,maximo =1,0,a[0]
	for i in a[1:]:
		if i<= maximo: lenght+=1
		else: lenght=1
		maximo=i
		if maxlen<lenght: maxlen=lenght
	return maxlen

def linear_algorithm_x(A):
	return max(longest_notgrowing(A),longest_growing(A))
'''
print(is_monotonic([1,2,3], 0, 2))
print(is_monotonic([1,1,7,7,9], 0, 4))
print(is_monotonic([9,9,5], 0, 2))
print(is_monotonic([6,6,6,6,6,6], 2, 4))
print(is_monotonic([1,1,1,2,1,3], 0, 5))
print(is_monotonic([1,1,1,2,1,3], 0, 3))
print(is_monotonic([3,2,1,3,2,1], 0, 5))
print(is_monotonic([3,2,1,3,2,1], 2, 3))
print(is_monotonic([3,2,1,3,2,1], 2, 4))
print(is_monotonic([3,2,1,3,2,1], 3, 5))
print(is_monotonic([7,4,7], 0, 2))
print(is_monotonic([7,4,7], 1, 2))
'''
#print(linear_algorithm_x([1,2,3,3,3,3,2,1,1,1,1]))