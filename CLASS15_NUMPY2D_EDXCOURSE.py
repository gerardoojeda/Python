# Import the libraries

import time
import sys
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline

#----------------------------------------------------------------------------------
# Plotting functions

def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.show()


def Plotvec2(a, b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

#--------------------------------------------------------------------------------------
# Create a python list

a = ["0", 1, "two", "3", 4]
print(a[0:3])
# Create a numpy array
print(type(a))
a =np.array([0,1,2,3,4])
a
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print(type(a))
# Check the type of the values stored in numpy array
print(a.dtype)
# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(b.dtype)
# Create numpy array and chaange numbers by index
c = np.array([20, 1, 2, 3, 4])
c[0]=100
print(c)
#slicing # Slicing the numpy array
d = c[1:4]#puts the values form one to 3 in d
print(d)
#set the values fomr position 3 and 4 to 300 and 400
c[3:5]=300,400
print(c)
#we can use a list to index or asign values
select = [0, 2, 3]#this is the list
d=c[select]#this will asign the 0,2,3 values to d
print(d)
#get the size of an array
print(d.size)
# Get the number of dimensions of numpy array
print(d.ndim)
# Get the shape/size of numpy array
print(d.shape)
# Create a numpy array

a = np.array([1, -1, 1, -1])
print(a)
#geat the mean
mean=a.mean()
print(mean)
# Get the standard deviation of numpy array

standard_deviation=a.std()
print(standard_deviation)
# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b
#get the minimum value
print(b.min())
#get the maximum value
print(b.max())
#--------------------------------------------------------------------------
#ARRAY OPERATIONS
u = np.array([1, 0])
u
v = np.array([0, 1])
v
# Numpy Array Addition or SUM
z = u + v
z
Plotvec1(u,z,v)
#-----------------------------------------------------------------------
#MULTIPLICATION
y = np.array([1, 2])
y
# Numpy Array Multiplication
z = 2 * y
z
print(z)
#--------------------------------------------------------------------------
#PRODUCT MULTIPLICATION
# Create a numpy array
v = np.array([3, 2])
v

u = np.array([1, 2])
u
z=u*v
print(z)
#--------------------------------------------------------------------------
#DOT PRODUCT
Dot=np.dot(v,u)
print(Dot)
#----------------------------------------------------------------------------
# Create a constant to numpy array
u = np.array([1, 2, 3, -1])
u
# Add the constant to array
u=u + 1
print(u)
#------------------------------------------------------------------------------
#MATHEMATICAL
# The value of pi
np.pi
# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])
print(x)
y=np.sin(x)
print(y)
#A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval. We specify the starting point of the sequence and the ending point of the sequence.
# The parameter "num" indicates the Number of samples to generate, in this case 5:
#
# Makeup a numpy array within [-2, 2] and 5 elements

print(np.linspace(-2, 2, num=5))
# Make a numpy array within [-2, 2] and 9 elements

print(np.linspace(-2, 2, num=9))
# Make a numpy array within [0, 2π] and 100 elements

x = np.linspace(0, 2*np.pi, num=100)
y=np.sin(x)
plt.plot(x,y)
plt.show()