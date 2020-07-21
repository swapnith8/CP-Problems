# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	x  = len(a)
	if(x%2==1):
		return a[x//2]
	elif(x==0):
		return None
	else:
		return (a[x//2]+a[(x//2)-1])/2