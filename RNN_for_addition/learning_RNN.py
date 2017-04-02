#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
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
learning_constant = 1
S = 100 #its high for time testing
output_size = S 
hidden_size = S
count = -1
T = 5 # https://arxiv.org/pdf/1301.3781.pdf
g4 = open('random_numbers.txt','r')
input = np.array([ [int(float(y)) for y in x.split() ] for x in g4 ])#numbers from 0 to 19
print input.shape
g4.close()

W = 1000

while True:
	sum_of_errors = 0
	sum_of_predicted_sums = 0
	sum_of_right_sums = 0
	#loss = 0
	count = count + 1
	h = []
	x = []
	y = []
	o = []
	r = []
	result = []
	i = 0
	while (i < 5):
		temp = np.zeros((S,1))
		r.append(input[count%W,i])
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
	#print "h[0].shape" 
	#print h[0].shape 
	#j = 0
	#while (j <= 5):
	#	print "h[j].shape: ",
	#	print h[j].shape
	#	j += 1
	#
	t = 0
	while (t < 5):
		h[t] = np.tanh(np.dot(Wx, x[t]) + np.dot(Wh, h[t-1]) ) #idiot! 
		#if(count % W == 0):
		#	print "t: ", t
		#	print "h1",np.dot(Wx, x[t])
		#	print "h2",np.dot(Wh, h[t-1])
	#	print "t"
	#	print t
	#	print "h[t].shape" 
	#	print h[t].shape 
	#	print "Wy.shape"
	#	print Wy.shape
		#print Wh
		#print Wx
		#print Wy
		y[t] = np.dot(Wy, h[t])
		#print "A"
		#print "t: ", t
		#print "y", y[t]
		y[t] = np.exp(y[t])
		exp_sum = 0
		for sth in y[t]:
			exp_sum += sth
		
		#print "sum: ", exp_sum
		
		y[t] = y[t]/exp_sum 
		
		#print y
		b = 0
		a = 0
		for j in range (len(y[t])) :
			if (b <= y[t][j]):
				b = y[t][j]
				a = j
		o[t] = a
		result[t] = result[t-1] + r[t]
		sum_of_errors += abs(a - result[t])
		#print "B"
		#print "t: ", t
		#print "y", y[t]
		#print "y[t][result[t]]: ", y[t][result[t]]
		loss -= (np.log(y[t][result[t]]))/(5*W)
		t += 1	
	
	if(count % W == 0):
		"""
		u = open('matrix_hidden_hidden.txt','w')
		A = S #hidden size
		B = S #hidden size
		#print Wh.shape
		for f in range(A):
			for i in range (B):
				u.write(str(Wh[f,i]))
				u.write(' ')
			u.write('\n')
		u.close()		

		u = open('matrix_output_hidden.txt','w')
		A = S #output size
		B = S #hidden size
		for f in range(A):
			for i in range (B):
				u.write(str(Wy[f,i]))
				u.write(' ')
			u.write('\n')
		u.close()		

		u = open('matrix_input_hidden.txt','w')
		A = S #input size
		B = S #hidden size
		for f in range(A):
			for i in range (B):
				u.write(str(Wx[f,i]))
				u.write(' ')
			u.write('\n')
		u.close()
		"""
		j = 0
		#if (y[1] == y[2]):
		#	print "BAD1"
		#if (y[2] == y[3]):
		#	print "BAD2"
		#if (y[3] == y[4]):
		#	print "BAD3"
		while (j <= 4):
			print result[j],
			print " ",
			j += 1
		print "N"
		j = 0
		while (j <= 4):
			print r[j],
			print " ",
			j += 1
		print "N"
		
		j = 0
		while (j <= 4):
			print o[j],
			print " ",
			j += 1
		print "N"
		
		print "count"
		print count		
		print "loss"
		print loss
		print "sum_of_errors"
		print sum_of_errors
		loss = 0
		#b = raw_input()	
	
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

