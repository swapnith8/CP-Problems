# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	d = str(n)
	if len(d) == 1:
		return n
	elif len(d)==2:
		if d[0] <= d[1]:
			return int(d[0])
		else:
			return int(d[1])		
	else:
		x = -1
		c = 0
		for i in range(len(d)-1):
			if (d[i]==d[i+1]):
				x = d[i]
				c = c+1
		if c>0:
			return int(x)		