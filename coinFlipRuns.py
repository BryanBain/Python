#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:37:35 2020

@author: bryanbain
"""

import random as rd

flip = ['h', 't']

results = ''

num_trials = 1000
num_successes = 0

for _ in range(num_trials):
    # simulate 200 flips of a coin
    for _ in range(200):
        results += rd.choice(flip)
    
    # determine if 6 heads or 6 tails in a row happened
    for i in range(len(results)-1):
        if results[i:i+6] == 'h'*6 or results[i:i+6] == 't'*6:
            num_successes += 1
            break
    
print(f"In {num_trials} simulations of 200 coin flips each, the number of "
      f"times either 6 heads or 6 tails occured in a row is {num_successes}")
