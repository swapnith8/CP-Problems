# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.
import math

def fun_carrylessadd(x, y):
	s= 0
	if (x == 0):
		 return y	
	if (y==0):
		return x
	n = 1
	sum = 0
	while x or y:
		sum = ((x%10) +(y%10))%10
		s = (sum *n)+s
		x = math.floor(x /10)
		y = math.floor(y/10)
		n = n *10	
	t = str(s)
	t.strip("0")
	return s


	