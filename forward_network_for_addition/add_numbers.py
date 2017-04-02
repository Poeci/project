#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import numpy as np

#sieć neuronowa dodaje 2 cyfry 
liczby = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

g1 = open('matrix_input_hidden.txt','r')
Wx = np.matrix([[float(y) for y in x.split()] for x in g1])
g1.close()

g3 = open('matrix_output_hidden.txt','r')
Wy = np.matrix([[float(y) for y in x.split()] for x in g3])
g3.close()

output_size = 20 
hidden_size = 20

while 1:
	h = np.matrix([[float(0)] for i in range(hidden_size)])
	x = np.matrix([[float(0)] for i in range(hidden_size)])
	y = np.matrix([[float(0)] for i in range(hidden_size)])
	first_num = np.random.randint(0,10)
	second_num = np.random.randint(0,10)
	result = first_num + second_num
	x[first_num] = 1;
	x[second_num] = 1;
	
	print first_num
	print second_num
	print result

	A = np.dot(Wx, x)
	h = np.tanh(A)
	y = np.dot(Wy, h)
	y = np.dot(Wy, h)
	#softmax function
	y = np.exp(y)
	exp_sum = 0
	for sth in y:
		exp_sum += sth
	y = y/exp_sum 
	#softmax function

	b = 0
	a = 0
	for j in range (len(y)) :
		if (b <= y[j]):
			b = y[j]
			a = j
	
	print "asd"
	print a
	a = int(raw_input())
	print a
