# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	
	x =[]
	y= []
	a =0
	b=0
	r1 = 0
	r2 =0
	for i in L:
		s = 0
		for j in i:
			s = s +j
		x.append(s)

	for i in range(len(x)):
		if(x.count(x[i]==1)):
			a = i	
			r2 = x[i]	
		elif(x.count(x[i]>1)):
			r1 =x[i]

	for i in range(len(L)):
		s =0
		for j in range(len(L)):
			s = s+L[i][j]
		y.append(s)

	for i in range(len(y)):
		if(y.count(y[i]==1)):
			b=i
	r = r2 - r1
	if(r>0):
		L[a][b]=L[a][b] - r
	else:
		L[a][b] =L[a][b] +r

	return L									