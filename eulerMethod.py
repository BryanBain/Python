"""
Purpose: Solve differential equations using Euler's method
Author: Bryan Bain
Date: July 30, 2020
File Name: eulerMethod.py
"""

import numpy as np
import math

# Initial conditions
x = 1
y = -1

dx = 0.5  # Step size

x_n = 5  # Last value of x

# The function itself
f = lambda x,y: y**2/np.sqrt(x)

# number of iterations
num_iters = int((x_n-x)/dx)+1

print(f'x \t\t y \t\t\t f(x,y)')
for i in range(num_iters):
  print(f'{x:0.2f} \t {y:0.6f} \t {f(x,y):0.6f}')
  y += dx*f(x,y)
  x += dx
