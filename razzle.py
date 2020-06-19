import random as rd
# import numpy as np

num_games = 0
die = [1, 2, 3, 4, 5, 6]

total_points = 0
total_cost = 0
cost_per_game = 1
sum = 0

half = [40, 17, 39, 16]
one_and_a_half = [42, 15, 41, 14]
five = [45, 13, 10, 11, 44, 12, 43]
eight = [46, 9, 47]
ten = [8, 48]

# num_games_played = []
# amount_spent = []

# while the total points is less than 10
while total_points < 10:

    # roll 8 dice
    for i in range(8):
        sum += rd.choice(die)

    num_games += 1

    # determine outcome from chart
    if sum == 29:
        cost_per_game *= 2
    elif sum in half:
        total_points += 0.5
    elif sum in one_and_a_half:
        total_points += 1.5
    elif sum in five:
        total_points += 5
    elif sum in eight:
        total_points += 8
    elif sum in ten:
        total_points += 10

    sum = 0
    total_cost += cost_per_game

print("You have played {} games.".format(num_games))
print("You have spent a total of ${:,}.".format(total_cost))

# num_games_played.append(num_games)
# amount_spent.append(total_cost)
#
# avg_num_games = np.mean(num_games)
# avg_amt_spent = np.mean(amount_spent)
#
# print("The average number of games you will play is {:,}".format(avg_num_games))
# print("The average amount you will spend each game is ${:,}".format(avg_amt_spent))
