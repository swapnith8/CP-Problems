# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	nStr = str(n)
	dStr = str(d)
	revStr = nStr[len(nStr)::-1]
	# print (revStr)

	if(k>=len(nStr)):
		revStr += dStr
	# print(revStr)	
	
	x = revStr[k]
	nStr = revStr[len(revStr)::-1]	
	y =""
	if (n<0):
		y += "-"
		for i in range(len(nStr)):
			if(nStr[i]!= x):
				y += nStr[i]
			
			else:
				y += dStr
	else:
		for i in range(len(nStr)):
			if(nStr[i]!= x):
				y += nStr[i]
			
			else:
				y += dStr

	return int(y)