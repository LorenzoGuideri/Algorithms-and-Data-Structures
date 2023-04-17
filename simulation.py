#!/usr/bin/python3.10 

def peak_element(A):
    a,i,b=0,len(A)//2,len(A)
    while A[i-1]>A[i] or A[i]<A[i+1]:
        if A[i]<A[i+1]:
            a=i
        else:
            b=i
        i=(a+b)//2
    else:
        return i

# It's O(log n)

def count_battleships(A):
    ships=0
    for y in range(len(A)):
        for x in range(len(A[0])):
            if A[y][x]== 'X':
                if y!=0 and A[y-1][x]=='X' or x!=0 and A[y][x-1]=='X':
                    pass
                else: ships+=1
    return ships

# The complexity is O(n*m), so O(n^2)

def ALgo_X(A,B):
    if len(A)!=len(B): return False
    C,D=A,B
    C.sort()
    D.sort()
    return C==D

def find_min_rectangle(points):
    points.sort(key=lambda x:x[1])
    points.sort(key=lambda x:x[0])
    hors=[]
    for i in range(len(points)-1):
        if points[i][0]==points[i+1][0]:
            hors.append([points[i][1],points[i+1][1],points[i][0]])
    minimo=0
    hors.sort(key=lambda x:x[0])
    for j in range(len(hors)-1):
        if hors[j][0]==hors[j+1][0] and hors[j][1]==hors[j+1][1]:
            if minimo==0 or minimo>(abs(hors[j][0]-hors[j][1])*abs(hors[j][2]-hors[j+1][2])):
                minimo=(abs(hors[j][0]-hors[j][1])*abs(hors[j][2]-hors[j+1][2]))
    return minimo



if __name__ == "__main__":
    #print(peak_element([1,2,1,3,5,6,4]))
    #print(count_battleships([['X','O','O','X'], ['O','O','O','X'], ['O','X','O','X'],['O','X','O','O']]))
    #print(find_min_rectangle([[1,1], [1,3], [3,3], [3,1], [2,2]]))
    #print(find_min_rectangle([[1,1], [1,3], [3,1], [3,3], [4,1], [4,3]]))
    #print(find_min_rectangle([[1,1], [1,3], [3,1]]))
    #print(find_min_rectangle([[1,1], [1,3], [3,1]]))
    print(find_min_rectangle([[3,2],[0,0],[3,3],[3,4],[4,4],[2,1],[4,3],[1,0],[4,1],[0,2]] ))
