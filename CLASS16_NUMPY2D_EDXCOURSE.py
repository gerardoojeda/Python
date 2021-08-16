# Import the libraries

import numpy as np
import matplotlib.pyplot as plt
# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)
print(type(a))
# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A
print(A)
# Show the numpy array dimensions
print(A.ndim)
#show the numpy array shape
print(A.shape)
# Show the numpy array size
print(A.size)
# Access the element on the second row and third column
print(A[1,2])
# Access the element on the second row and third column
print(A[1][2])
# Access the element on the first row and first column
print(A[0][0])
# Access the element on the first row and first and second columns
print(A[0,0:2])
# Access the element on the first and second rows and third column
print(A[0:2,2])
#--------------------------------------------------------------------------------------------
#BASIC OPERATIONS
# Create a numpy array X
X = np.array([[1, 0], [0, 1]])
X
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]])
Y
#ADD THEM UP
Z=X+Y
print('z',Z)
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]])
Y
#multiply all elements by a single one
Z = 2 * Y
Z
# Element-wise product of the array X and Y as follows:
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]])
Y
# Create a numpy array X
X = np.array([[1, 0], [0, 1]])
X
Z=Y*X
print(Z)
#----------------------------------------
#matrix multiplication  with the numpy arrays A and B
# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
print(A)
# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
print(B)
# Calculate the dot product
Z = np.dot(A,B)
print(Z)
# Calculate the sine of Z
np.sin(Z)
# Create a matrix C

C = np.array([[1,1],[2,2],[3,4]])
print(C)
print(C.T)