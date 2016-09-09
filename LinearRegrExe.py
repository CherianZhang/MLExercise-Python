#!/usr/bin/env python
import numpy as np

#/Users/zhangyanyan/zyyproject/MachineLearning-Cherian/ex2Data

f_x = open('/Users/zhangyanyan/zyyproject/MachineLearning-Cherian/ex2Data/ex2x.dat')
x = []
#print type(x)	
for line in f_x.readlines():	
	flx = float(line)
	x.append(flx)

arrx_t = np.array(x)
len = arrx_t.shape

arrx = arrx_t.T 

#print arrx

f_x.close()

f_y = open('/Users/zhangyanyan/zyyproject/MachineLearning-Cherian/ex2Data/ex2y.dat')
y = []

for line in f_y.readlines():
	fly = float(line)
	y.append(fly)

arry = np.array(y)

f_y.close()

theta = [0,0]
arrthe = np.array(theta)
thresh = 0.00198
arrthe1 = arrthe 

print arrthe1

alpha = 0.07
m = 0.02
times = 1500 
count =0

sqsum = 1

sumy = arry.sum()

TrainX = np.array([np.ones(50), arrx])
#print TrainX

while count < times:
	arrthe = arrthe1
	sum = 0
	product = 0
	#to calculate sum from 1 to m on (theta*xi - yi)*xi  [the equation is derivation function]	
	sum = arrthe.dot(TrainX) - arry
	sum = sum.dot(TrainX.T)

	product = alpha * m * sum
	#print product
	#update the value of theta
	arrthe1 = arrthe - product

	count = count +1;
	#print count	
print arrthe1 

