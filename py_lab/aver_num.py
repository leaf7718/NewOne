#!/usr/bin/python
import sys

loopnum = int(input("input the number of numbers : "))
x = 0
tmp = 0
cnt = 0
while loopnum != 0:
	tmp = int(input(""))
	x += tmp
	loopnum -= 1
	cnt += 1
avr = x/cnt
print("average of numbers : %f" % avr)


