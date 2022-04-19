import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from numpy import linalg as LA

def print_plane_eq(n, c) : 
    print(n[0], "x +", n[1], "y +", n[2], "z -", c, "= 0")

n1 = np.array([2,2,-3])
n2 = np.array([2,5,3])

c1 = 7
c2 = 9

e1 = np.array([[1],
               [0],
               [0]])
e3 = np.array([[0],
               [0],
               [1]])

lamda = int((np.dot(n1,e3) - np.dot(n1,e1))[0] / (np.dot(n2,e1) - np.dot(n2,e3))[0])

n = n1 + lamda * n2
c = c1 + lamda * c2

print("The equation of the required plane is :-")
print_plane_eq(n, c)