#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
u = open('matrix_hidden_hidden.txt','w')
A = 512 #hidden size
B = 512 #hidden size
for f in range(A):
	for i in range (B):
		u.write(str(np.random.random_sample()))
		u.write(' ')
	u.write('\n')
u.close()		

