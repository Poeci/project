#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
u = open('matrix_input_hidden.txt','w')
S = 148
A = S #input size
B = S #hidden size
for f in range(A):
	for i in range (B):
		u.write(str(np.random.random_sample()*0.1 + 0.001))
		u.write(' ')
	u.write('\n')
u.close()		

