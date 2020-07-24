# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def ishappynumber(n):
    if n<1:
        return False
    else:
        if n == 1:
            return True
        else:
            s = 0
            t = n
            while t>0:
                r = t%10
                s += r*r
                t = t//10
            if s == 1 or s ==4:
                if s ==1:
                    return True
                else:
                    return False    
            else:
                return ishappynumber(s)

def isprime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
        else:
            return True

    return False

def fun_nth_happy_prime(n):
    x = []
    number = 2
    while len(x) != n+1:
        if ishappynumber(number) and isprime(number):
            x.append(number)
        number +=1

    return x[n]        
	