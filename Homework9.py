"""
Week 8 Homework #9
Purpose:
    - Write a program that can find the minimum of a function that you define. The function can be any one (even very simple) as long as it actually has a minimum. You are welcome to use any standard or external C++ or Python libraries (you don't need to implement the minimization routine, only the function to be minimized). You can also try to visualize your function and the location of the minimum (not required).

    - Some possible minimization libraries/methods you can use (with examples):

        [Python]

            - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
            - https://scipy-lectures.org/advanced/mathematical_optimization/index.html

@author: @aelieber1
date: March 27, 2023
"""

# import packages
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# define function
def g(x):
    return x**2 + 10*np.sin(x)

# find minimum value
min = minimize(g, x0=0)
min_val = float(min.x)
print(min)

# plot function and identify minimum
x = np.arange(-10,10,0.1)
plt.plot(x, g(x), label='function g(x)')
plt.plot([float(min.x)], [g(min_val)], marker='*', ms=20, label='minimum value')
plt.title("Function with Minimum Identified through Scipy.Optimize.Minimize")
plt.legend()
plt.show()


