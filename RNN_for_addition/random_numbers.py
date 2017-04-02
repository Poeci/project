#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import numpy as np
u = open('random_numbers.txt','w')
A = 10000 #input size
B = 5 #hidden size
for f in range(A):
	for i in range (B):
		u.write(str(np.random.random_sample()*20))
		u.write(' ')
	u.write('\n')
u.close()		

