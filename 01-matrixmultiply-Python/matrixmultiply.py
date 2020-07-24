# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    x = len(m1[0])
    y = len(m2)
    l = []
    if (x == y ):
        for i in range(0,len(m1)):
            t = []
            for j in range(0,len(m2[0])):
                n = 0
                for k in range(0,len(m1[0])):
                    n += m1[i][k] * m2 [j][k]
                t.append(n)
        return t
    else:
        return None




