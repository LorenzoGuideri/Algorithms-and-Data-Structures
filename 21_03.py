#!/usr/bin/python3

def gcd(a,b):
	return gcd(b,a%b) if b else a

def rotate(l,offset):
    for num in range(1 if gcd(len(l),offset)==1 else gcd(len(l),offset)):
        pos=num
        val=l[num]                    														# we begin to work on the first number
        for i in range(len(l) if gcd(len(l),offset)==1 else len(l)//gcd(len(l),offset)):	# make swaps trough all the array
            pos=(pos+offset)%len(l)  
            val,l[pos]=l[pos],val
    return l

# print(rotate( [1, 2, 3, 4, 5, 6], 4))

# for ex 2 just copy the is_growing(), it's the same

def arr_to_tups(A):             # auxiliary to save the points as structures
    return [(A[x],A[x+1]) for x in range(0,len(A),2)]

def sort_by(A,c):               # sort the list of point relatively to the c_th element of the point
    A.sort(key=lambda x:x[c])
    return A

def list_vertical(A):           # sort the array relatively to the x cooridnate of the points, if two points share the same x they make a vertical line. append the line to the array
    B=[]
    A=sort_by(arr_to_tups(A),0)
    for i in range(len(A)-1):
        if A[i][0]==A[i+1][0]:
            B.append([A[i],A[i+1]])
    return B

def list_horizontal(A):         # same principle, but with the y's
    B=[]
    A=sort_by(arr_to_tups(A),1)
    for i in range(len(A)-1):
        if A[i][1]==A[i+1][1]:
            B.append([A[i],A[i+1]])
    return B

def count_horizontal(A):        # do I seriously have to explain it?
    return len(list_horizontal(A))

def count_vertical(A):
    return len(list_vertical(A))

def intersect(A):               # analyze in O(n^2) if there are any lines intersecting.
    verts=list_vertical(A)
    hors=list_horizontal(A)
    for v in verts:
        for h in hors:
            if h[0][0] < v[0][0] and v[0][0] < h[1][0] and v[0][1] < h[0][1] and h[0][1] < v[1][1]: # a stupid way to understand if two lines are intersecting.
                return True
    return False

# print(count_vertical([1,2,1,3,1,4,2,5]))
# print(count_horizontal([1,1,3,1]))
# print(intersect([1,1,3,1,2,0,2,4]))
# print(intersect( [1,2,1,3,2,1,2,2] ))
