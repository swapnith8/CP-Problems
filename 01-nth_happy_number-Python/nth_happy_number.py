# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def find(n):
	s = 0
	while(n>0):
		x =n%10
		s = s+(x)*(x)
		n = n//10
	return s

def ishappynum(n):
	if(n<=0):
		return False
	s =n
	while(s!= 1 and s!=4):
		s = find(s)
	if(s==1):
		return True
	else:
		return False		
def fun_nth_happy_number(n):
	x =[]
	for i in range(50):
		if ishappynum(i):
			x.append(i)
	return x[n]
