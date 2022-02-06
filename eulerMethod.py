"""
Purpose: Solve differential equations using Euler's method
Author: Bryan Bain
Date: July 30, 2020
File Name: eulerMethod.py
"""

import numpy as np
import math

def eulerMethod(x_0, y_0, h, x_n, func):
	"""
	:param x_0: initial x value
	:param y_0: initial y value
	:param h: step size
	:param x_n: last value of x
	:param func: lambda function that y' equals
	"""
	num_iters = int((x_n-x_0)/h)+1
	print(f'x \t\t y \t\t\t f(x,y)')
	for i in range(num_iters):
  		print(f'{x_0:0.2f} \t {y_0:0.6f} \t {func(x_0,y_0):0.6f}')
  		y_0 += h*func(x_0,y_0)
  		x_0 += h

eulerMethod(0, 1, 0.1, 1, lambda x,y: x-y)
