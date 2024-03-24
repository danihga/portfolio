import random
from scipy.misc import derivative
import numpy as np

########################################################
# Question 4
########################################################

## Solver Funtion
## Inputs -- a funtion, initial guess, tolerance
def newtonsMethod(f, f_prime, x0, tolerance):
    ## Creates a list with the initial guess at position 0,
    ## Where each iteration will be appended
    iter_list = [x0]
    
    ## Variable which gives the last positions 
    ## in the list
    position = 0
    #print(x0)
    ## Infinite Loop
    while(True):
        
        ## Newton's Method formula
        x0 = x0 - (f(x0)/f_prime(x0))
        
        ## Appends the iteration to the list
        iter_list.append(x0)
        print(x0)
        
        ## Increases by one as a new item
        ## Has been added to the list
        position += 1
        
        ## Conditional statement that checks if the difference 
        ## Between the two last items are smaller than the tolerance
        ## If true, breaks the infinite loop and returns 
        ## iter_list
        if abs(iter_list[position]-iter_list[position-1])<tolerance:
            return iter_list
            break
########################################################
# Question 5
########################################################

def f(x):
    return x**4-4*x**3-x**2+10*x
       
def f_prime(x):
    return 4*x**3-12*x**2-2*x+10
#print(newtonsMethod(f, f_prime, 1, 0.00001))
'''

[2.87, -266.66555244096696, -199.7524334170983, 
 -149.56868385817532, -111.93232465281729, 
 -83.7069925778363, -62.54057673111723, 
 -46.669209372327245, -34.77027714037882, 
 -25.85220373811244, -19.171819678338416, 
 -14.17243412029709, -10.437450231130983, 
 -7.655663764669061, -5.595365234237764, 
 -4.085115739454981, -2.999650518815309, 
 -2.2497667250868516, -1.7746681635806951, 
 -1.5304716642155431, -1.4563200411276895, 
 -1.4495443452176238, -1.449489746312622, 
 -1.449489742783178]

It should approximate to 0

'''

########################################################
# Question 6
########################################################

# Second derivative it's not continuous at x=0
def f2(x):
    return x**(1/3)
       
def f2_prime(x):
    return (1 / 3) * x ** (-2/3)

'''

(3.5991310356045747e+162-8.470307470724576e+148j)
(-7.198262071208925e+162+1.6940614941448622e+149j)
(1.43965241424174e+163-3.4310914204307946e+149j)
(-2.8793048284833913e+163+6.862182840861376e+149j)...

And we get an error message

'''
########################################################
# Question 7
########################################################

# Polynomial of order 6
def f3(x):
    return (x-4)*(x-3)*(x-1)*(x+1)*(x+2)*(x+3)

# Derivative of f3
def f3_prime(x):
    return 6*x**5-10*x**4-72*x**3+60*x**2+178*x-18

# A function which generates 1000
# sequences using Newtons method at 
# a funtion from random points in an 
# interval of (-10,10)
def thousandIter(f, f_prime):
    
    # Creates a list
    list1000 = []
    
    # Loop over it 1000 times
    for i in range(1000):
        
        # Generates a random real number from -10 to 10
        randomx0 = random.randint(-10,10) + random.random()
        
        # Generates a sequence using Newtons Method and
        # appends it to list1000
        list1000.append(newtonsMethod(f, f_prime, randomx0, 0.000001))
    
    # Returns the list with the 1000 sequences
    return list1000

########################################################
# Question 8
########################################################

# This function estimates the order of convergence
# Inputs -- funtion and its derivative
# Order of Convergence of 1000 starting point at f3
def orderOfConvergence(f, f_prime):
    
    # Invokes funtion thousand Iter to generate a list
    # with 1000 different iterstarting point iterations
    # on the function f3
    list1000 = thousandIter(f, f_prime)
    averageOrder = 0
    
    # Loops over the 1000 iterations
    for i in range(1000):
        
        # Copies a unique approximation to the list l
        l = list1000[0]
        
        # s calculates the number of iterations in that
        # precise approximation
        s = len(l)-1
        
        # Find the approximate order of convergence
        # Using the last 4 iterations of the sequence
        up = np.log(abs((l[s]-l[s-1])/(l[s-1]-l[s-2])))
        down = np.log(abs((l[s-1]-l[s-2])/(l[s-2]-l[s-3])))
        q = up / down
        averageOrder += q
    
    # Returns the average order of convergence of the 1000 root 
    # approximations
    return averageOrder/1000
    
print(orderOfConvergence(f3, f3_prime))
'''

Answer = 2.0004442894049235 

Aproximately order  of convergence 2
Off by 0.0004

'''