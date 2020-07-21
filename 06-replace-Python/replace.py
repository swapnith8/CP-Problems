# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	b = ''
	for x in s1:
		if x!= s2:
			b+=x
		else:
			b+=s3
	return b		
	# l = len(s2)
	# s =""
	# i = 0
	# while(i<len(s1)):
	# 	if(s1[i:i+l]==s2):
	# 		s+=s3
	# 		i=i+l
	# 	else:
	# 		s+=s1[i]
	# 		i=i+l
	# return s

