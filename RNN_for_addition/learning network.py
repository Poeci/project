#!/usr/bin/python 
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np

#Vanila RNN with cross-entropy-loss that is learning how to make prefix sums for 5 numbers. Numbers are intigers from {0,1,...,19}.
g1 = open('matrix_input_hidden.txt','r')#random matrix 100x100
Wx = np.array([[float(y) for y in x.split()] for x in g1])
g1.close()

g2 = open('matrix_hidden_hidden.txt','r')#random matrix 100x100
Wh = np.array([[float(y) for y in x.split()] for x in g2])
g2.close()

g3 = open('matrix_output_hidden.txt','r')#random matrix 100x100
Wy = np.array([[float(y) for y in x.split()] for x in g3])
g3.close()

loss = 0
learning_constant = 0.05
S = 100 
output_size = S 
hidden_size = S
count = -1

T = 5
W = 10000


while True:
	count = count + 1
	sum_of_errors = 0
	sum_of_predicted_sums = 0
	sum_of_right_sums = 0
	loss = 0
	h = []
	x = []
	y = []
	o = []
	r = []
	result = []
	i = 0
	while (i < 5):
		temp = np.zeros((S,1))
		r.append(np.random.randint(0,20))
		h.append(temp)
		y.append(temp)
		temp[r[i]] = 1
		x.append(temp)
		o.append(0)
		result.append(0)
		i += 1	
	result.append(0)
	temp = np.zeros((S,1))
	h.append(temp)		
	t = 0
	while (t < 5):
		h[t] = np.tanh(np.dot(Wx, x[t]) + np.dot(Wh, h[t-1]) ) #idiot! 
		if(count % W == 0):
			print "t: ", t
			print "h1",np.dot(Wx, x[t])
			print "h2",np.dot(Wh, h[t-1])
		y[t] = np.dot(Wy, h[t])
		y[t] = np.exp(y[t])
		exp_sum = 0
		for sth in y[t]:
			exp_sum += sth
		y[t] = y[t]/exp_sum 
		b = 0
		a = 0
		for j in range (len(y[t])) :
			if (b <= y[t][j]):
				b = y[t][j]
				a = j
		o[t] = a
		result[t] = result[t-1] + r[t]
		sum_of_errors += abs(a - result[t])
		loss -= (np.log(y[t][result[t]]))
		t += 1	
	
	loss /= 4
	if(count % W == 0):
		
		j = 0
		while (j <= 4):
			print result[j],
			print " ",
			j += 1
		print "\n"
		j = 0
		while (j <= 4):
			print r[j],
			print " ",
			j += 1
		print "\n"
		
		j = 0
		while (j <= 4):
			print o[j],
			print " ",
			j += 1
		print '\n'
		
		print "count"
		print count		
		print "loss"
		print loss
		print "sum_of_errors"
		print sum_of_errors
	
	t = 4
	deltahnext = np.zeros((S, 1))
	hprev = np.zeros((S, 1))
	deltaWy = np.zeros_like(Wy)
	deltaWh = np.zeros_like(Wh)
	deltaWx = np.zeros_like(Wx)
	
	h[-1] = hprev
	while (t >= 0):
		deltay = y[t]
		deltay[result[t]] -= 1
		deltah = Wy.T * deltay + deltahnext
		deltahraw = (1 - h[t] * h[t]) * deltah
		deltaWy += deltay * h[t].T
		deltaWx += deltahraw * x[t].T
		deltaWh += deltahraw * h[t-1].T
		deltahnext = Wh.T * deltahraw
		t -= 1
	
	Wx -= learning_constant * deltaWx
	Wy -= learning_constant * deltaWy
	Wh -= learning_constant * deltaWh
		
