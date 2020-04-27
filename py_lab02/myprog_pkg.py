#!/usr/bin/python
from my_pkg import conv_boh
from my_pkg import uandi_int
import re
import sys

menu = 0
while menu!=3:
	menu = int(input("Select menu: 1)conversion 2)union/intersection 3)exit ?"))
	if menu==1:
		bin = int(input("input binary number: "))
		conv_boh.conv(bin)
	elif menu==2:
		lst1 = re.findall("\d+", input("1st list : "))
		lst2 = re.findall("\d+", input("2nd list : "))
		uandi_int.uandi(lst1, lst2)
	else:
		print("exit the program.")

sys.exit()
