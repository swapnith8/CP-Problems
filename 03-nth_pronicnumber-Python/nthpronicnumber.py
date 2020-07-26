# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math
def pronicnumber(n):
	# Your code goes here
	x = 0
	while(x<=int(math.sqrt(n))):
		if n== x*(x+1):
			return True
		x = x+1
	return False

def nthpronicnumber(n):
	l = []
	for i in range(4000):
		if pronicnumber(i):
			l.append(i)
	return l[n]		
