# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	disx = math.sqrt(((x2-x1)**2) +((y2 -y1)**2))
	disy = math.sqrt(((x3-x1)**2)+((y3-y1)**2))
	disz = math.sqrt(((x1-x3)**2)+((y1-y3)**2))
	if(disx == math.sqrt((disy**2)+(disz**2))):
		return True
	elif(disy == math.sqrt((disx**2)+(disz**2))):
		return True
	elif (disz == math.sqrt((disy**2)+(disx**2))):
		return True
	else:
		return False		
