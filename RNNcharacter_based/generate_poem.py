#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np

znaki = [ '\x83', '\x98', '\x96', '\xa1', '\x97', '\xb6', '\xad',
'\xef', '\xbb', '\xbf', 'j', '\xc4', '\x99', '\xc3', '\xb3', '\xe2', '\x80', '\x94', '\xc5', '\x82', '\xbc', '\x9b', '\x85', '\xba', '\x87', '\x84', '\x9a', '\xa9', '\xa6', '\xc2', '\xab', '\x93', '\x81', '\xa0', '\xb9', '\x86'
,'<','>','/','@','#','$','%','^','&','*','-','\\','_','+','=','|','0','1','2','3',
'4','5','6','7','8','9',';','"','\'','{','[','(',')','}',']',' ', '\n', '	',':' ,'.','?','!',',',
'A','Ą','E','Ę','O','U','Ó','Y', 'I',
'a','ą','e','ę','o','u','ó','y', 'i',
'J','D','T','R','P','B','Q','X','S','Ś','Z','Ż','Ź','C','Ć','K','H','G','F','W','V','L','Ł','M','N','Ń'
'j','d','t','r','p','b','q','x','s','ś','z','Ż','ź','c','ć','k','h','g','f','w','v','l','ł','m','n','ń' ]


g1 = open('matrix_input_hidden.txt','r')
Wx = np.matrix([[float(y) for y in x.split()] for x in g1])
g1.close()

g2 = open('matrix_hidden_hidden.txt','r')
Wh = np.matrix([[float(y) for y in x.split()] for x in g2])
g2.close()

g3 = open('matrix_output_hidden.txt','r')
Wy = np.matrix([[float(y) for y in x.split()] for x in g3])
g3.close()

#print Wx
#print Wh
#print Why
## potrzeba rozmiaru ukrytego 
output_size = 148 #
hidden_size = 148
h = np.matrix([[float(0)] for i in range(hidden_size)])
g4 = open('poems_in_numbers.txt','r')
xf = np.matrix([int(float(y)) for x in g4 for y in x.split() ]) ## musi być zgodność z input size i musza być liczby z rozsadnego zakresu
xf = xf.T
input_size = 10
#print input_size-1
g4.close()
## wiersz o określonej długości - 500
wiersz = open('result_poem.txt', 'w')

for i in range(input_size-1):
	#print i
	#print int(xf[i])
	temp = [float(0) for k in range(hidden_size)]
	#print temp[0]
	#print len(temp)
	#print temp[1] 
	#print i 
	temp[int(xf[i])] = 1
	
	x = np.matrix(temp)
	x = x.T
	A = np.dot(Wh, h)
	B = np.dot(Wx, x)
	h = np.tanh(A + B)
	
temp = [float(0) for jk in range(hidden_size)]
#print input_size-1
temp[xf[(input_size-1)]] = 1
x = np.matrix(temp)
x = x.T
for i in range(input_size-1,500):
	A = np.dot(Wh, h)
	B = np.dot(Wx, x)
	h = np.tanh(A + B)
	y = np.dot(Wy, h)
	y = np.dot(Wy, h)
	#xp = [x.item(i) for i in range(input_size)]
	#xp.pop(0)
	#xp.append(y.item(0))
	#x =  np.matrix([[float(xp[i])] for i in range(input_size)])
	
	#softmax function
	y = np.exp(y)
	exp_sum = 0
	for sth in y:
		exp_sum += sth
	y = y/exp_sum # softmax function
	#y_tab[i] = y
	maximum = -10
	max_ind = 0
	a = np.random.random()
	#print a
	b = 0
	for j in range (len(y)) :
		b += y[j]
		if (b >= a):
			maximum = y[j]
			max_ind = j
			break
	temp = [float(0) for i in range(hidden_size)]
	temp[max_ind] = 1
	x = np.matrix(temp)
	x = x.T
	wiersz.write(str(znaki[max_ind]))
