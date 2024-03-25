import numpy as np
from scipy import optimize
import cvxopt
import random
import matplotlib.pyplot as plt

# Function to calculate the deviation of a harmonic
def harmonic(n, step):
    
    return ((1200/step) * np.log2(n))


# Generates a random step for each harmonic
def steps():
    fundamental = []
    steps = []
    position = list(range(1,24))
   
    # Generates a list with the position of the 
    # Fundamental harmonic and the other 3 harmonics
    for i in range(5):
        x = random.randrange(0,len(position))
        fundamental.append(float(position[x]))
        position.pop(x)
    
    # Calculates the difference in position between 
    # The harmonics and the fundamental and returns
    # A list with the relative positions of the harmonics
    # With respect to the fundamental
    for i in range(1,5):
        steps.append(float(fundamental[i]-fundamental[0]))
    return steps

# Function that finds the minmax solution
# Output -- An array with the minimum harmonic deviation
# Given the random steps 
def findMinMax(harmonic, step):
    
    # Steps of the constraints
    
    
    #harmonics = [5/4, 7/4, 9/8, 11/8]
    
    # Objective Function
    c = np.array([0.0, 1.0])
    
    # Constraints
    b = np.array([harmonic(5/4, step[0]), 
                  -1*harmonic(5/4, step[0]), 
                  harmonic(7/4, step[1]), 
                  -1*harmonic(7/4, step[1]), 
                  harmonic(9/8, step[2]), 
                  -1*harmonic(9/8, step[2]), 
                  harmonic(11/8, step[3]), 
                  -1*harmonic(11/8, step[3])])
    # Constraints of variables
    A = np.array([[step[0], -1.0],
                 [step[0], -1.0],
                 [step[1], -1.0],
                 [step[1], -1.0],
                 [step[2], -1.0],
                 [step[2], -1.0],
                 [step[3], -1.0],
                 [step[3], -1.0]])
    
    A_ = cvxopt.matrix(A)
    b_ = cvxopt.matrix(b)
    c_ = cvxopt.matrix(c)
    
    sol = cvxopt.solvers.lp(c_, A_, b_)
    xy = np.array(sol['x'])
    
    return xy
#print(steps())

# 
x = []
y = []
positions = []

# Runs the function findMinMax(harmonic, steps) 10,000 times
for i in range(10000):
    step = steps()
    sol = findMinMax(harmonic, step)
    # Appends the distance between keys to x
    x.append(sol[0][0])
    
    # Appends the deviation to y list
    y.append(sol[1][0])
    
    # Appends the positions to the positions list
    positions.append(step)

print(step)
    
# Create the vectors X and Y
x = np.array(x) 
y = np.array(y)


# Create the plot
plt.scatter(x, y, s = 0.5)

plt.xlabel("x")
plt.ylabel(" MinMaxDeviation ")
# Show the plot
plt.show ()
        
    