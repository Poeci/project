#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
## tablica znaków w kolejności, znaki "podobne" sa blisko siebie, sortowanie zrobione ręcznie
znaki = [ '\x83', '\x98', '\x96', '\xa1', '\x97', '\xb6', '\xad',
'\xef', '\xbb', '\xbf', 'j', '\xc4', '\x99', '\xc3', '\xb3', '\xe2', '\x80', '\x94', '\xc5', '\x82', '\xbc', '\x9b', '\x85', '\xba', '\x87', '\x84', '\x9a', '\xa9', '\xa6', '\xc2', '\xab', '\x93', '\x81', '\xa0', '\xb9', '\x86'
,'<','>','/','@','#','$','%','^','&','*','-','\\','_','+','=','|','0','1','2','3',
'4','5','6','7','8','9',';','"','\'','{','[','(',')','}',']',' ', '\n', '	',':' ,'.','?','!',',',
'A','Ą','E','Ę','O','U','Ó','Y', 'I',
'a','ą','e','ę','o','u','ó','y', 'i',
'J','D','T','R','P','B','Q','X','S','Ś','Z','Ż','Ź','C','Ć','K','H','G','F','W','V','L','Ł','M','N','Ń'
'j','d','t','r','p','b','q','x','s','ś','z','Ż','ź','c','ć','k','h','g','f','w','v','l','ł','m','n','ń' ]
#print len(znaki)
#print znaki

f = open('poems.txt', 'r')
grre = open('ewa.txt', 'w')

for c in f:
	for e in c: 
		g = 1
		for a in znaki:
			if (e == a):
				g = 0
		if (g == 1):
#			grre.write(e)
			print 'zlo'
			znaki.append(e)
grre.write( str(znaki))
print len(znaki)