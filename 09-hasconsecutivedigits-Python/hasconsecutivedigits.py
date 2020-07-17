# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	Str = str(n)
	l = split(Str)
	print(l)

	# for i in range(n):
	# 	Str[i]=Str[i+1]
	# print (Str)	

	