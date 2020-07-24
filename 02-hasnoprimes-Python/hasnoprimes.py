# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	for i in range(len(l)):
		for j in range(len(l[i])):
			x = l[i][j]
			y = 1
			c =0
			while(x>y):
				if(x%y==0):
					c +=1
					y+=1
				else:
					y+=1
			if c<=1:
				return False			
	return True

