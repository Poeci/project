#!/usr/bin/python 
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
#2 layers neural forward network with cross-entropy-loss that is learning how to double intiger from {1,2,..,10} 
g1 = open('matrix_input_hidden.txt','r')#random matrix 20x20
Wx = np.array([[float(y) for y in x.split()] for x in g1])
g1.close()

g3 = open('matrix_output_hidden.txt','r')#random matrix 20x20
Wy = np.array([[float(y) for y in x.split()] for x in g3])
g3.close()

loss = 0
learning_constant = 1
output_size = 20 
hidden_size = 20
count = 0
while 1:
	loss = 0
	count = count + 1
	
	h = np.zeros((20,1))
	x = np.zeros((20,1))
	y = np.zeros((20,1))
	
	first_num = np.random.randint(0,10)
	second_num = 2
	result = first_num * second_num
	x[first_num] = 1
	xt = x.T
	A = np.dot(Wx, x)
	h = np.tanh(A)
	ht = h.T
	y = np.dot(Wy, h)
	yt = y.T
	y = np.exp(y)
	exp_sum = 0
	for sth in y:
		exp_sum += sth
	y = y/exp_sum 

	b = 0
	a = 0
	for j in range (len(y)) :
		if (b <= y[j]):
			b = y[j]
			a = j
	loss -= (np.log(y[result]))
	deltay = y
	deltay[result] -= 1
	Wx -= learning_constant*((1-h*h)*(Wy.T*deltay)*xt)
	Wy -= learning_constant*(deltay*ht)		
	if(count % 3 == 0):
		print "count"
		print count
		print "loss"
		print loss
		print count
		print "a - result"
		print a - result
		b = raw_input()
