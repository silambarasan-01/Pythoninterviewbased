# Python3 implementation of the above approach

def check(ch):

	if (ch >= 'A' and ch <= 'Z'):
		print(ch,"is an UpperCase character");

	elif (ch >= 'a' and ch <= 'z'):
		print(ch,"is an LowerCase character");
	else:
		print(ch,"is not an aplhabetic character");

print(check("B"))
