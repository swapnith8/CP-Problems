# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def verify(n):
	s = 0
	while(n>0):
		s = s+(n%10)*(n%10)
		n=n//10
	return s		
def fun_nth_happy_prime(n):
	n = n+ 1
	i = 0
	c= 0
	while(c<n):
		i +=1
		s = i
		while(s!=1 and s!=4):
			s=sum(s)
		j = 1
		y = 0
		if(s==1):
			while(j<=i):
				if(i%j==0):
					y=y+1
			if(y==2):
				c=c+1	
	return i