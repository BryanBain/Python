from fractions import Fraction

A = 600
B = 300
C = 100

bet_amount = 50

total = A + B + C
percent = 0.03
profit = total * percent

probA = (profit - B - C) / (-1*A) 
probB = (profit - A - C) / (-1*B) 
probC = (profit - A - B) / (-1*C) 

payA = bet_amount*(1 + probA)
payB = bet_amount*(1 + probB)
payC = bet_amount*(1 + probC)

print(f'A: {Fraction(probA).limit_denominator()}')
print(f'B: {Fraction(probB).limit_denominator()}')
print(f'C: {Fraction(probC).limit_denominator()}')

print(f'Bet Amount: ${bet_amount}') 

print(f'A Payout: ${payA:0.2f}')
print(f'B Payout: ${payB:0.2f}')
print(f'C Payout: ${payC:0.2f}')
