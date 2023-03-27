#!/usr/bin/python3.10 
 
def sort(array):
	if len(array)<2:
		return array
	mid=len(array)//2
	one,two,i,j,three=sort(array[:mid]),sort(array[mid:]),0,0,[]
	while i<len(one) and j<len(two):
		if one[i]<two[j]:
			three.append(one[i])
			i+=1
		else:
			three.append(two[j])
			j+=1
	three+=one[i:]
	three+=two[j:]
	return three


if __name__ == '__main__':
	print(sort([5, 2, 8, 3, 6, 1, 7, 4]))
