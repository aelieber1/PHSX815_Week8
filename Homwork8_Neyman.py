"""
Week 8 Homework #8
Purpose:
    - Write code for a simple model with at least one parameter (like coin probability, normal distr. mean, etc.) and an observable related to that parameter

    - Create a figure of the "Neyman Construction" (see March 23 lecture), i.e. make a 2D plot with "true" parameter value on the x-axis and "measured" value on the y-axis, sampling many random experiments for each true value 

    - Bonus (not worth additional points) - pretend that you did the experiment and measured a particular value of the parameter. What are the "error"'s/what is the posterior distribution for the parameter after the measurement? (you can get this from your 2D plot by looking at the 1D slice from the 2D histogram corresponding to the "measured" value).

    - Create a GitHub repository for your code and submit the URL via Canvas

@author: @aelieber1
date: March 24, 2023
"""

# Import packages
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import seaborn as sns

# Import Random class
from Random import Random

mu_true_values = []
mu_best_values = []

# Define parameters
Nmeas = 1
Nexp = 100000
mu_experiment = 2
mu_true = 0
mu_best = 0
sigma = 2

for i in range(-100,101):
    mu_true = float(i)/10
    
    # loop over experiments
    for e in range(Nexp):
        mu_best = 0
        
        # loop over measurements
        for m in range(Nmeas):
            #x = np.random.poisson(mu_true)
            x = np.random.normal(loc=mu_true, scale=sigma)
            
            # add up all measurements
            mu_best += x
            
        mu_best = mu_best / float(Nmeas)
        
        mu_true_values.append(mu_true)
        mu_best_values.append(mu_best)
        
x = mu_true_values
y = mu_best_values

#print("Mu_true: ", mu_true_values)
#print("Mu_best: ", mu_best_values)


# Index that matches the mu_experiment
#index = mu_best_values.index(mu_experiment)
#print("index: ", index)

# Plot a 2 Dimensional Histogram of this data
#ax = sns.regplot(x, y, ci=80)
plt.hist2d(x, y, bins=100)
plt.xlabel("#mu true")
plt.ylabel("#mu measured")
plt.title("Neyman Construction - Gaussian Function")
plt.show()