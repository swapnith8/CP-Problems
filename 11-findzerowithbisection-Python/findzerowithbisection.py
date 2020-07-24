# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.
import math
def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't change these values
	# epsilon
	# your code starts here
	mid = (1+x)/2
	if (findzerowithbisection(1,epsilon)*findzerowithbisection(mid,epsilon)<0):
		mid1 =(1+mid)/2
		findzerowithbisection(mid1,epsilon)
	if(findzerowithbisection(mid,epsilon)*findzerowithbisection(x,epsilon)<0):
		mid2 =(mid+x)/2
		findzerowithbisection(mid2,epsilon)
