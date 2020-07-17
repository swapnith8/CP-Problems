# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	Str = str(n)
	c = list(Str)
	# print(c)

	for i in range(len(c)+1):
		if(c[i]==c[i+1]):
			return True
		# else:
		# 	return False	

	