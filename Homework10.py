"""
Week 9 | Homework #10
PHSX 815 | Spring 2023

@author: aelieber1
date: March 31, 2023

Purpose:
- Write a program that can find the minimum of a function that you define. Unlike homework #9, the function must now be at least 2-dimensional (higher dimensions fine too - doesn't have to be complicated). You are welcome to use any standard or external C++ or Python libraries (you don't need to implement the minimization routine, only the function to be minimized). 

Although none of these are explicitly required for this homework, these are additional elements you are encouraged to explore as you are completely these assignments:

- Can you visualize the function you are minimizing? Can you visualize the location of the minimum found?

- Can you extract from the minimization result information about the estimated "error" on your minimum? Can you calculate how many function calls were used in the minimization? 

- Can you compare different algorithms in the minimization? Do you observe any differences?

 
Some possible minimization libraries/methods you can use (with examples): [Python]
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
- https://scipy-lectures.org/advanced/mathematical_optimization/index.html


Tutorial help:
- utilized this tutorial to help especially with visualizations:
    - https://medium.com/analytics-vidhya/3d-visualization-of-a-function-of-two-variables-from-ℝ²-into-ℝ-with-python-matplotlib-5bd3df39fc94
    
"""

# import packages
from scipy.optimize import minimize
from scipy.optimize import rosen, rosen_der
import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

# define function with 2 variables
#def obj(x,y):
   #return np.sin(x)*np.cos(y)
def obj(params):
    x, y = params
    return 2*x**2 - x*y + 2*y**2

# visualize function
# Choose a range of values from set of real numbers for x an y
x = np.linspace(-100,100,100)
y = np.linspace(-100,100,100)

# Create an array of calues containing all pairs (xi,yi) for xi in x and yi in y
XY = np.meshgrid(x, y)
X, Y = np.meshgrid(x, y)

# Compute vlaues of our function for each defined pair
Z = obj(XY)

# Visualize plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet', edgecolor='none')

ax.set_title("Surface", fontsize = 13)
ax.set_xlabel("x", fontsize = 11)
ax.set_ylabel("y", fontsize = 11)
ax.set_zlabel("f(x,y)", fontsize = 10)
plt.show()

# minimize function
initial_guess = [0,0]
res = minimize(obj, initial_guess, method='BFGS')
# error check help from stack overflow (https://stackoverflow.com/questions/13670333/multiple-variables-in-scipys-optimize-minimize)
if res.success:
    fitted_params = res.x
    print("Minimum found at: ", fitted_params)
    print("Full Minimization Details: \n", res)
else:
    raise ValueError(result.message)
    
"""
Full explanation of all of the attributes from the OptimizeResult object found here in the Scipy docs: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult
"""