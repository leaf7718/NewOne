#!/usr/bin/python

def conv(x):
	input = str(x)
	result = 0
	for i in range(len(str(x))):
		result = (x%(10**(i+1)))//(10**i)*(2**i) + result

	print("OCT : {}".format(oct(result)))
	print("DEC : {}".format(result))
	print("HEX : {}".format(hex(result)))

if __name__== '__main__':
	print("this is conv_boh.py")
