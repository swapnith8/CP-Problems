# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	x = []
	s = ""
	for i in range(len(text)):
		x.append(text[i])
	y =x[:]
	for i in range(0,len(x)-2):
		for i in  range(i+1,len(x)):
			if(x[i]==x[j]):
				y[j]=="not valid"
	for i in y:
		if(i=="not valid"):
			s+=i	
	return s	