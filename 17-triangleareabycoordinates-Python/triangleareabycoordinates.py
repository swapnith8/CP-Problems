# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math
def trianglearea(disx,disy,disz):
	s = (disx + disy + disz) /2
	area = math.sqrt ((s)*(s-disx)*(s-disy)*(s-disz))
	return area
def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here

	disx = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	disy = math.sqrt(((x3-x2)**2)+((y3-y2)**2))
	disz = math.sqrt(((x1-x3)**2)+((y1-y3)**2))
	A = trianglearea(disx,disy,disz)
	return A