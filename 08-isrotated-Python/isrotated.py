# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	
	if len(str1)!= len(str2) or str1 ==str2:
		return False
	else:
		temp =str1+str1
		if str2 in temp :
			return True
		else:
			return False		
	