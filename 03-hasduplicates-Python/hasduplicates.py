# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	l = []
	for i in L:
		for j in i:
			l.append(j)
	l1 = set(l)
	if (len(l)==len(l1)):
		return False	
	return True		