#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
g1 = open('matrix_input_hidden.txt','r')
Wxh = np.matrix([[float(y) for y in x.split()] for x in g1])
g1.close()

g2 = open('matrix_hidden_hidden.txt','r')
Whh = np.matrix([[float(y) for y in x.split()] for x in g2])
g2.close()

g3 = open('matrix_output_hidden.txt','r')
Why = np.matrix([[float(y) for y in x.split()] for x in g3])
g3.close()

#print Wxh
#print Whh
#print Why
## potrzeba rozmiaru ukrytego 
output_size = 1
hidden_size = len(Whh)
h = np.matrix([[float(0)] for i in range(hidden_size)])
g4 = open('start.txt','r')
x = np.matrix([[float(y)] for x in g4 for y in x.split() ]) ## musi być zgodność z input size i musza być liczby z rozsadnego zakresu
input_size = len(x)

g4.close()
## wiersz o określonej długości - 500
wiersz = open('roboczy_wiersz_w_liczbach.txt', 'w')
for i in range(500):

	A = np.dot(Whh, h)
	B = np.dot(Wxh, x)
	h = np.tanh(A + B)
	y = np.dot(Why, h)
	xp = [x.item(i) for i in range(input_size)]
	xp.pop(0)
	xp.append(y.item(0))
	x =  np.matrix([[float(xp[i])] for i in range(input_size)])
	
	wiersz.write(str(y.item(0)));
	wiersz.write(' ');
