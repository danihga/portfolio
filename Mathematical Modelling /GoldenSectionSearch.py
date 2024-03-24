import random
import math
import numpy as np

# Constant which takes the value of the golden number
phi = (1 + math.sqrt(5)) / 2

## Solver Funtion
## Inputs -- lower point of interval, higer point of interval, tolerance, 
## constat phi, funtion
## Output -- List with the average of the interval after every loop

def goldenMethod(a, b, tolerance, phi, f):
    
    ## Creates a list which will contain the average of a and b 
    ## from every loop
    iter_list = []
    
    ## Check if a<b, if not swiches the values
    if (a>b):
        x = a
        a = b
        b = x
    
    ## Calls funtions to get middle point
    c = getc(a, b, phi)
    d = getd(a, b, phi)
    
    ## Creates and infinite loop 
    while (True):
       
        
        ## Checks if the the difference b-a is smaller than the tolerance
        if ((b-a>tolerance)):
            
            ## b-a is bigger than the desired tolerance
            ## Estimated minimum is taken from 
            ## the average of a and b
            avg = (a+b)/2
            
            ## Appends the average to the iter_list
            iter_list.append(avg)
        
            ## If f(d) is greater than f(c)
            ## b gets the value of d
            ## d the value from c
            ## and new c is calculated
            if (f(d)>f(c)):
                b = d
                d = c
                c = getc(a, b, phi)
            
            ## If f(c) is greater than f(d)
            ## a gets the value of c
            ## c the value from d
            ## and new d is calculated
            else:
                a = c
                c = d
                d = getd(a, b, phi)
        
        ## b-a is smaller than the tolerance hence we exit the infinite loop
        ## and return the list which contains the estimated minimum for 
        ## each iteration
        else:
            
            return iter_list
            break
'''
print(goldenMethod(-10,10, 0.0000001,phi, f) )    
[0.0, -3.819660112501052, -1.4589803375031547, -2.917960675006309, 
 -2.0162612375115665, -1.4589803375031543, -1.8033988749894845, 
 -1.5905365124674025, -1.4589803375031543, -1.5402865250609878, 
 -1.4900365376545728, -1.5210927378059915, -1.5018989505509952, 
 -1.4900365376545728, -1.497367912013147, -1.501898950550995, 
 -1.4990986147302694, -1.5008293174473917, -1.4997596843437884, 
 -1.5004207539573073, -1.5000121904672228, -1.4997596843437884, 
 -1.4999157417104383, -1.5000121904672228, -1.4999525818573574, 
 -1.4999894220042762, -1.5000121904672228, -1.4999981187832503, 
 -1.5000068155622244, -1.5000014406572255, -1.4999981187832503, 
 -1.5000001718142735, -1.4999989029713212, -1.4999996871593921, 
 -1.5000001718142735, -1.4999998722810841, -1.5000000574027759, 
 -1.4999999429912783, -1.5000000137014724, -1.499999970000169]
'''
    
## Method which returns value of c
## Inputs -- Both interval points, constant phi
def getc(a, b, phi):
   
    ## c is calculated
    return b + ((a-b)/phi)

## Method which returns value of d
## Inputs -- Both interval points, constant phi
def getd(a, b, phi):
     
    # d is calculated
    return a + ((b-a)/phi)

## Another polynomial of order 2
def f(x):
    return x**2+3*x+5

## Another polynomial of order 2
def f_1(x):
    return x**2+4*x+3

# Polynomial of order 6
def f_3(x):
    return (x-4)*(x-3)*(x-1)*(x+1)*(x+2)*(x+3)
        
 

# A function which generates 1000
# sequences using Newtons method at 
# a funtion from random points in an 
# interval of (-10,10)

def thousandIter(f, phi):
    
    # Creates a listph
    list1000 = []
    
    # Loop over it 1000 times
    for i in range(1000):
        
        # Generates a random real number from -10 to 10
        randomA = random.randint(-10,10) + random.random()
        randomB = random.randint(-10,10) + random.random()
        
        # Generates a sequence using Newtons Method and
        # appends it to list1000
        list1000.append(goldenMethod(randomA, randomB, 0.0001, phi, f))
    
    # Returns the list with the 1000 sequences
    return list1000

#print(thousandIter(f_3, phi))

# This function estimates the order of convergence
# Inputs -- funtion and phi
# Output -- List with order of convergence from 1000 tries
def orderOfConvergence(f, phi):
    
    # Invokes funtion thousand Iter to generate a list
    # with 1000 different iterstarting point iterations
    # on the function f3
    list1000 = thousandIter(f, phi)
    orderOfConvergence = []
    averageOrder  = 0
  
    # Loops over the 1000 iterations
    for i in range(1000):
        
        # Copies a unique approximation to the list l
        l = list1000[i]
        # s calculates the number of iterations in that
        # precise approximation
        s = len(l)-1
        
        # Find the approximate order of convergence
        # Using the last 4 iterations of the sequence
        up = np.log(abs((l[s]-l[s-1])/(l[s-1]-l[s-2])))
        down = np.log(abs((l[s-1]-l[s-2])/(l[s-2]-l[s-3])))
        q = up / down
        orderOfConvergence.append(q)
        averageOrder += q

    
    # Returns the average order of convergence of the 1000 minima
    # approximations
    print(averageOrder/1000)
    return orderOfConvergence

'''
print(orderOfConvergence(f_3,phi))

order of convergence aprox. => 1.0000000000012934
'''