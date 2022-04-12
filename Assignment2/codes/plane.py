import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from numpy import linalg as LA

def print_plane_eq(n, c) : 
    print(n[0], "x +", n[1], "y +", n[2], "z -", c, "= 0")

n1 = np.array(([2,2,-3]))
n2 = np.array(([2,5,3]))

c1 = 7
c2 = 9

lamda = 5

n = np.add(n1, lamda * n2)
c = c1 + lamda * c2

print("The equation of the required plane is :-")
print_plane_eq(n, c)