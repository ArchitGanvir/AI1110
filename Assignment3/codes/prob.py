import numpy as np
from numpy import random as RN

red = 3
black = 5

#Total number of balls in the bag - Sample size
N = red + black

#Theoretical probabilities
Pr_0 = red / N
Pr_1 = black / N
print("Theoretical probabilities are :-")
print("(i)", Pr_0)
print("(ii)", Pr_1)

#Random/Experimental Probabilities

#Generating events
X = RN.randint(0, high = 2, size = N)

count0 = np.count_nonzero(X==0)
count1 = np.count_nonzero(X==1)

Pr_0 = count0 / N
Pr_1 = count1 / N

print("Random probabilities are :-")
print("(i)", Pr_0)
print("(ii)", Pr_1)