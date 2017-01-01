#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
g1 = open('matrix_input_hidden.txt','r')
Wxh = np.matrix([[float(y) for y in x.split()] for x in g1])
#print Wxh.shape
dWxh = np.zeros_like(Wxh)
g1.close()

g2 = open('matrix_hidden_hidden.txt','r')
Whh = np.matrix([[float(y) for y in x.split()] for x in g2])
#print Whh.shape
dWhh = np.zeros_like(Whh)
g2.close()

g3 = open('matrix_output_hidden.txt','r')
Why = np.matrix([[float(y) for y in x.split()] for x in g3])
#print Why.shape
dWhy = np.zeros_like(Why)
g3.close()

output_size = 148 #
hidden_size = len(Whh)
h = np.matrix([[float(0)] for i in range(hidden_size)])
y = np.matrix([[float(0)] for i in range(output_size)])
g4 = open('poems_in_numbers.txt','r')
xf = np.matrix([int(float(y)) for x in g4 for y in x.split() ])#numbers from 0 to vocabulary_size - 1, here 148
xf = xf.T
input_size = len(xf)# must be more than 1
input_size = 200
#print input_size
#print input_size
h_tab = [h for k in range(input_size - 1)]
y_tab = [y for k in range(input_size - 1)]
g4.close()
#possible outer loop
loss = 0
learning_constant = 0.05
#forward
for k in range (100):
	for xi in range (0,input_size-100,100):
		h = np.matrix([[float(0)] for wer in range(hidden_size)])
		for i in range(xi,xi+90):
			temp = [float(0) for k in range(hidden_size)]
			temp[xf[i]] = 1
			x = np.matrix(temp)
			temp[xf[i]] = 0
			x = x.T
			x[xf] = 1
		#	print x.shape
			A = np.dot(Whh, h)
			B = np.dot(Wxh, x)
		#	print B.shape
		#	print A.shape 
			h = np.tanh(A + B)
			h_tab[i] = h
			y = np.dot(Why, h)
			#softmax function
			y = np.exp(y)
			exp_sum = 0
			for sth in y:
				exp_sum += sth
			y = y/exp_sum # softmax function
			y_tab[i] = y
			maximum = -10
			max_ind = 0
			for j in range (len(y)) :
				if (y[j] > maximum):
					max_ind = j
			
			temp[xf[i+1]] = 1
			perfect_output = np.matrix(temp)
			perfect_output = perfect_output.T
		#	loss -= (np.log(y[xf[i+1]]))
		#loss = loss/(input_size-1) #cross entropy loss
		#backward
		for i in range(xi,xi+90):
			j = 2*xi+90 - i - 1
			copy_y = y_tab[j]
			copy_y[xf[j+1]] -= 1
			delta = np.dot(Why.T,copy_y)
			#print h_tab[j]
			#dh_j = 1 - h_tab[j]*h_tab[j]
			
			dh_j = h_tab[j]	
			for i in range(len(dh_j)) : 
				dh_j[i] = 1 - dh_j[i]*dh_j[i]  #(tanh(x))' = 1 - tanh^2(x)
			delta = dh_j.T*delta
			dWhy += np.dot(copy_y , h_tab[j].T) ##!!?
			temp = [float(0) for k in range(output_size)]
			temp[xf[j]] = 1
			x = np.matrix(temp)
			dWxh += delta*x
			dWhh += delta*(h_tab[j].T)
		
		#...
		Whh -= dWhh*learning_constant
		Wxh -= dWxh*learning_constant
		Why -= dWhy*learning_constant

u = open('matrix_hidden_hidden.txt','w')
A = 148 #hidden size
B = 148 #hidden size
#print Whh.shape
for f in range(A):
	for i in range (B):
		u.write(str(Whh[f,i]))
		u.write(' ')
	u.write('\n')
u.close()		

u = open('matrix_output_hidden.txt','w')
A = 148 #output size
B = 148 #hidden size
for f in range(A):
	for i in range (B):
		u.write(str(Why[f,i]))
		u.write(' ')
	u.write('\n')
u.close()		

u = open('matrix_input_hidden.txt','w')
A = 148 #input size
B = 148 #hidden size
for f in range(A):
	for i in range (B):
		u.write(str(Wxh[f,i]))
		u.write(' ')
	u.write('\n')
u.close()