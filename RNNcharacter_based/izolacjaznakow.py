#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
znaki = []
f = open('pan-tadeusz.txt', 'r')
for c in f:
	for e in c: 
		g = 1
		for a in znaki:
			if (e == a):
				g = 0
		if (g == 1):
			znaki.append(e)
for r in znaki :
	print r,
	print ' ',
