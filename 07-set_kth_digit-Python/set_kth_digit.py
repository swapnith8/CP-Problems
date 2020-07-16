# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	nStr = str(-468)
	dStr = str(1)
	revStr = nStr[::-1]
	print (revStr)
	StrLen = len(nStr)
	if(3>=StrLen):
		revStr += 1
	x = nStr[3]
	y =""
	if (-468<0):
		y += "-"
		for i in range(StrLen):
			if(revStr[i]!= x):
				y += revStr[i]
				print (y)
			else:
				y += dStr
				# print(y)

	