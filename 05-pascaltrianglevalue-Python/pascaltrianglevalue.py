# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):

	list = [1]
	for i in range(row):
		list.append(int(list[i]*(row-i)/(i+1)))
	if col<len(list):
		return list[col]
	else:
		return 0	

	
