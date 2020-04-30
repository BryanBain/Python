import random
user = input("Choose your weapon: ")
comp = random.choice(['rock', 'paper', 'scissors'])

print("The user (you) chose", user)
print("The comp (I) chose", comp)

if user == comp:
    print("It's a tie")
elif user == 'rock' and comp == 'paper':
    print("I win!")
elif user == 'rock' and comp == 'scissors':
    print("You win!")
elif user == 'paper' and comp == 'scissors':
    print("I win!")
elif user == 'paper' and comp == 'rock':
    print("You win!")
elif user == 'scissors' and comp == 'rock':
    print("I win!")
elif user == 'scissors' and comp == 'paper':
    print("You win!")





