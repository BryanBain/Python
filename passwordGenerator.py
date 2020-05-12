"""
File: 	 passwordGenerator.py
Author:  Bryan Bain
Date: 	 May 12, 2020
Purpose: Randomly generate a password of ASCII characters.
"""

import random as rd

pw_length = 10
pw_list = []

for i in range(pw_length):
	pw_list.append(chr(rd.randint(33, 126)))

pw = ''.join(pw_list)

print(f"Your password is {pw}")
