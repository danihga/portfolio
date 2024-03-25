
"""
Created on Sun Mar 7 2021

@author: ddelasheras
"""
import random
import numpy as np
import matplotlib.pyplot as plt


## We read in the infromation from a text file
## And process it such that it is divided into 
## 721 experiemnts or rows with 11 columns of 
## For each experiment. We save it in the constant X

X = []
with open("data.txt") as f:
    for line in f:
        # convert each line to a list of strings
        line_to_list = line.strip('\n').strip('][').split(', ')
        # convert list of strings to list of ints and append to data list
        X.append([int(i) for i in line_to_list])
# convert data to numpy array
X = np.asarray(X)

## We compute the column mean range and standard deviation of the data matrix
## This provides some usefull information to interpret the data
## We use the funtions .mean, .std, .max, .min, .ptp to do this
mean_column = np.mean(X, axis=0)
min_column =  np.min(X, axis=0)
max_column = np.max(X, axis=0)
range_column = np.ptp(X, axis=0)
std_column = np.std(X, axis=0)


## We standarize the data by columns
## To do this we take the data matrix
## And subtract each column by its mean
## And divide each column by the standard deviation 
## Of its entries
n, m = X.shape
XNormed = (X - np.mean(X, axis=0))/np.std(X, axis=0)

## We compute the Covariance Matrix by left matrix multplication
## Of the data matrix X and its transpose
## We use the fucntion .matmul which performs matrix multiplications

C = np.matmul(X.T, X)

## We use the funtion .linalg.eig(c) to obtain
## Covariance matrix eigenvalues and corresponding eigenvectors
## And store them in two arrays: eigenvalues (stores eigenvalues)
## And eigenvectors (stores eigenvectors)

eigenvalues, eigenvectors = np.linalg.eig(C)

'''
variance_explained = []
for i in eigenvalues:
     variance_explained.append((i/sum(eigenvalues))*100)
print(variance_explained)
'''

## We know that the eigenvalues are sorted such that the largest
## Apear in the leftmost columns. Therefore to access the two
## Largest ones we must get the two first columns

## Principal components
pc1 = eigenvalues[0]
pc2 = eigenvalues[1]
print(pc1)
print(pc2)

## Their eigenvectors
pc_axis1 = eigenvectors[0].reshape(11,1)
pc_axis2 = eigenvectors[1].reshape(11,1)
print(pc_axis1)
print(pc_axis2)
## We create a basis matrix (variable eigen_basis) with both eigenvectors
## Using the method .cocatenate 
## And we use axes=1 as we want the vectors to be the columns of the matrix
## We then use .matul to multiply the data matrix with the eigen-basis
## This projects the dataset to the eigen-basis
eigen_basis = np.concatenate((pc_axis1,pc_axis2),axis=1)
data_proj = np.matmul(X, eigen_basis)

##############################################################################
## Scatter plot display
##############################################################################

plt.scatter(data_proj[:,0], data_proj[:,1], s=5)
plt.title("Music Symetry")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

##############################################################################
## Plot of data projected into two random directions
##############################################################################

## We generate random directions in which we project the data
## This show a very deficient spread of the data
## So little conclusion can be made
random_dir1 = np.random.rand(11,1)
random_dir2 = np.random.rand(11,1)
new_basis = np.concatenate((random_dir1,random_dir2),axis=1)
another_data_proj = np.matmul(X, new_basis)
plt.scatter(another_data_proj[:,0], another_data_proj[:,1], s=5, c="r")
plt.title("Data Projected Into Random Directions")
plt.xlabel("Random Direction 1")
plt.ylabel("Random Direction 2")
plt.show()

##############################################################################
## Plot of data projected into random principal components (not PC1 and PC2)
##############################################################################

## We project the data into random eigenvectors
## Which are not the ones that correpond to the
## Two first principal components
random_number1 = random.randint(2,10)
random_number2 = random.randint(2,10)
eigen_random1 = eigenvectors[random_number1].reshape(11,1)
eigen_random2 = eigenvectors[random_number2].reshape(11,1)

## Checks two vectors are not equal by using 
## The method .array_equal()
while np.array_equal(eigen_random1, eigen_random2, equal_nan=False):
    random_number2 = random.randint(2,10)
    eigen_random2 = eigenvectors[random_number2].reshape(11,1) 

another_new_basis = np.concatenate((eigen_random1, eigen_random2),axis=1)
and_another_data_proj = np.matmul(X, another_new_basis)
plt.scatter(and_another_data_proj[:,0], and_another_data_proj[:,1], s=5, c="r")
plt.title("Data Projected Into Two Difrerent PC{} and PC{}".format(random_number1+1, random_number2+1))
plt.xlabel("PC{}".format(random_number1+1))
plt.ylabel("PC{}".format(random_number2+1))
plt.show()





