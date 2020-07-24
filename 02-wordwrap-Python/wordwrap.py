# Write the function wordWrap(text, width) that takes a string of text (containing only lowercase letters
#  or spaces) and a positive integer width, and returns a possibly-multiline string that matches the 
# original string, only with line wrapping at the given width. So wordWrap("abc", 3) just returns "abc", 
# but wordWrap("abc",2) returns a 2-line string, with "ab" on the first line and "c" on the second line. 
# After you complete word wrapping in this way, only then: All spaces at the start and end of each 
# resulting line should be removed, and then all remaining spaces should be converted to dashes ("-"), 
# so they can be easily seen in the resulting string. Here are some test cases for you:
# assert(wordWrap("  abcdefghij", 4)  ==  """\
# abcd
# efgh
# ij""")

# assert(wordWrap(" a b c de fgh ",  4)  ==  """\
# a-b-
# c-de
# -fgh""")


def fun_wordwrap(s, n):
	str1 = s.strip().replace(" ","-")
	str2 = ""
	l = len(str1)
	for i in range(l):
		if i %n == 0 and i >0:
			str2 =str2 +"\n"+str1[i]
		else:
			str2 =str2 +str1[i]+""
	return str2


 