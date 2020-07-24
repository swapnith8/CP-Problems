"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	h , l , mid = []
	if(len(array)>1):
		pivot = array[0]
		for i in array:
			if i > pivot:
				h.append(i)
			if i<pivot:
				l.append(i)
			if i==pivot:
				mid.append(i)
		return l.sort()+mid+h.sort()	

	else:
		return array				