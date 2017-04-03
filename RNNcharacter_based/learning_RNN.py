#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
import shutil
g1 = open('matrix_input_hidden.txt','r')#random matrix 148x148
Wx = np.array([[float(y) for y in x.split()] for x in g1])
g1.close()

g2 = open('matrix_hidden_hidden.txt','r')#random matrix 148x148
Wh = np.array([[float(y) for y in x.split()] for x in g2])
g2.close()

g3 = open('matrix_output_hidden.txt','r')#random matrix 148x148
Wy = np.array([[float(y) for y in x.split()] for x in g3])
g3.close()
S = 148
output_size = 148 #
hidden_size = len(Wh)
h = np.matrix([[float(0)] for i in range(hidden_size)])
y = np.matrix([[float(0)] for i in range(output_size)])
g4 = open('poems_in_numbers.txt','r')
input = [int(float(y)) for x in g4 for y in x.split() ]#numbers from 0 to vocabulary_size - 1, here 148

input_size = len(input)# must be more than 1
W = 10000
#input_size = 240000
#print input_size
#print input_size
#h_tab = [h for k in range(input_size - 1)]
#y_tab = [y for k in range(input_size - 1)]
g4.close()
#possible outer loop
loss = 0
learning_constant = 0.001
T = 25
#forward
count = 0#2150000
while True:
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
	while (i < T):
		temp = np.zeros((S,1))
		r.append(input[(count + i)%input_size])
		h.append(temp)
		y.append(temp)
		temp[r[i]] = 1
		x.append(temp)
		o.append(0)
		result.append(input[(count+i+1)%input_size])
		i += 1
		
	count += T	
	
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
	while (t < T):
		h[t] = np.tanh(np.dot(Wx, x[t]) + np.dot(Wh, h[t-1]) ) #idiot! 
		hprev = h[t]
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
		##probably rand would be better!
		for j in range (len(y[t])) :
			if (b <= y[t][j]):
				b = y[t][j]
				a = j
		o[t] = a
		#result[t] = result[t-1] + r[t]
		#print "B"
		#print "t: ", t
		#print "y", y[t]
		#print "y[t][result[t]]: ", y[t][result[t]]
		loss -= (np.log(y[t][result[t]]))
		t += 1	
	
	if(count % W == 0):
		
		shutil.copy2('matrix_hidden_hidden.txt', 'matrix_hidden_hidden2.txt') 
		shutil.copy2('matrix_input_hidden.txt', 'matrix_input_hidden2.txt') 
		shutil.copy2('matrix_output_hidden.txt', 'matrix_output_hidden2.txt') 
		u = open('matrix_hidden_hidden.txt','w')
		A = 148 #hidden size
		B = 148 #hidden size
		#print Wh.shape
		for f in range(A):
			for i in range (B):
				u.write(str(Wh[f,i]))
				u.write(' ')
			u.write('\n')
		u.close()		

		u = open('matrix_output_hidden.txt','w')
		A = 148 #output size
		B = 148 #hidden size
		for f in range(A):
			for i in range (B):
				u.write(str(Wy[f,i]))
				u.write(' ')
			u.write('\n')
		u.close()		

		u = open('matrix_input_hidden.txt','w')
		A = 148 #input size
		B = 148 #hidden size
		for f in range(A):
			for i in range (B):
				u.write(str(Wx[f,i]))
				u.write(' ')
			u.write('\n')
		u.close()
		
		j = 0
		
		#if (y[1] == y[2]):
		#	print "BAD1"
		#if (y[2] == y[3]):
		#	print "BAD2"
		#if (y[3] == y[4]):
		#	print "BAD3"
		"""
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
		"""
		print "count"
		print count		
		print "loss"
		print loss
		#print "sum_of_errors"
		#print sum_of_errors
		#loss = 0
		#b = raw_input()	
	
	t = T - 1
	deltahnext = np.zeros((S, 1))
	if(count % 600 == 0):
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
