# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	list = []
	for row in range(1,row+1):
		list.append(1)

		for i in range(row - 2, 0, -1):
			list[i] += list[i-1]
		
	return (row,col,list)
