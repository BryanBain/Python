"""
birthday_simulator.py
Author: Bryan Bain
Date: April 29, 2020
Purpose: Simulate the probability that in a room of 23 people, 
at least 2 of them have the same birthday.
"""

import random as rd

def birthdayParadox(sample_size, num_simulations):
  """
  Calculates the probability that in a room with <sample_size> people in it,
  at least 2 of them share a birthday. 
  :param sample_size: the number of people in each sample. 
  :param num_simulations: the number of simulations of the experiment to run. 
  return: the probability that at least two people share a birthday.
  """
  dates = [_ for _ in range(1,366)]
  num_shared_birthdays = 0

  """
  Check if 2 values are the same by converting the list to a set (which will 
  eliminate duplicates) and then checking the lengths. Different lengths will 
  mean that there is a duplicate "date" in the sample. Do this several times.
  """
  for i in range(num_simulations):
    sample = [rd.choice(dates) for _ in range(sample_size)]
    if len(sample) != len(set(sample)):
      num_shared_birthdays += 1

  ratio = num_shared_birthdays/num_simulations

  return ratio

def main():
  result = birthdayParadox(23, 100_000)
  print(f"The probability that in a room of 23 people at least two of them "
  	f"share a birthday is about {100*result:.2f}%")

if __name__ == "__main__":
  main()