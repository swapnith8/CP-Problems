# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def ispowerfulnumber(n):
	x = 2
	while n >1:
		if n%x == 0:
			if n % (x**2) == 0:
				return True
				while n>1 and n%x ==0:
					n = n//x
			else:
				x = x+1
	return True			

def nthpowerfulnumber(n):
	# Your code goes here
	l = []
	for i in range(100):
		if ispowerfulnumber(i):
			l.append(i)
	print(l)
	return l[n+1]		
	
