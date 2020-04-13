#!/usr/bin/python
import sys

n = int(input("fibonacci number fn? : "))
F1 = F2 = 1
cnt = 2
Fn = 0
print("%d, %d" % (F1, F2),end="")
while cnt != n:
	Fn = F1 + F2
	print(", %d" % Fn,end="")
	F1 = F2
	F2 = Fn
	cnt += 1
print("\n")
print("F%d = %d" % (n, Fn))
