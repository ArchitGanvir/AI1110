import numpy as np
from numpy import random as RN

#Selecting arbitrary values for m,n
white = m = 3
black = n = 5

#Theoretical probability

Pr = 1
numerator_term = n
denominator_term = m + n - 1
Pr_i = 1
for i in range(1,int(n / 2) + 1):
    Pr_i *= (numerator_term * (numerator_term - 1)) / (denominator_term * (denominator_term - 1))
    Pr += Pr_i
    numerator_term -= 2
    denominator_term -= 2
Pr *= m / (m + n)

print("Theoretical probability is :-")
print(Pr)

#Random/Experimental Probability

A_wins = 0

#Repeating the experiment an arbitrary number of times
N = 1000
white_list = [0 for i in range(0,m)]
black_list = [1 for i in range(0,n)]
for i in range (0,N):
    box = white_list + black_list
    outcome = []
    for i in range(0,m + n):
        outcome.append(RN.choice(box))
        if outcome[i] == 0:
            break
    if i % 2 == 0:
        A_wins += 1

Pr = A_wins / N
print("Random probability is :-")
print(Pr)