# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def sumOfSquares(n):
    s = 0
    while n>0:
        r = n % 10
        s = s+(r**2)
        n = n//10
    return s    

def isHappyNumber(n):
    l = []
    while sumOfSquares(n) not in l:
        res = sumOfSquares(n)
        if res==1:
            return True
        else:
            l.append(res)
            n = res
    return False

def isprime(n):
    if n>1 :
        while n>2:
            i = 2
            if n%i == 0:
                return False
            return True
    return False
    
def ishappyprimenumber(n):
   # Your code goes here
    if isprime(n) and isHappyNumber(n):
       return True
    return False   
    