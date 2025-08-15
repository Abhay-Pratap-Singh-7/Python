import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# 1D array
a = np.array([1,2,3,4,5])

# 2D array
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# 3D array
c = np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]])

print(a)
print(b)
print(c)

# to know number of elements in array
print(a.size)
print(b.size)
print(c.size)

# to know rows and col
print(a.shape)
print(b.shape)
print(c.shape)

# to know type of data present in array
print(a.dtype)

# to transpose a array
print(b.transpose())

# to get random array of M x N matrix with specific data type
a = np.empty((3,3), dtype = int)
print(a)

# to initialize array with 1
x = np.ones((6,5), dtype=int)
print(x)

# to initialize array with 0
x = np.zeros((6,5), dtype=int)
print(x)

# to get a range of elements np.arange(start,end,step)
y = np.arange(1,20)
print(y)

z = np.arange(2,20,2)
print(z)

# to reshape an array
z = z.reshape((3,3))
print(z)

# to convert multi dimensional array to 1D array
z = z.flatten()
print(z)

# to convert multi dimensional array to 1D array
b = b.ravel()
print(b)

'''Difference between ravel() and flatten()
    Ravel() is fast as it changes original dataset and does not use extra storage
    Flatten() is slow as it make a copy and uses extra storage to store the copy'''

a = np.arange(1,19).reshape((3,6))
b = np.arange(20,38).reshape((3,6))
print(a)
print(b)

# to add corresponding elements of array
print(np.add(a,b))

# to subtract corresponding elements of array
print(np.subtract(a,b))

# to multiply corresponding elements of array
print(np.multiply(a,b))

# to divide corresponding elements of array
print(np.divide(a,b))

# to multiply matrix Note : shapes should be MxN and NxP
b = b.reshape((6,3))
print(a@b)

# to find min and max from any array
print(b.max())
print(b.min())

# to get sum of all elements of array
print(b.sum())

# to get sum of row and col
print(np.sum(b, axis=1)) # for row 
print(np.sum(b, axis=0)) # for column

# to get mean of all elements
print(np.mean(b))

# to get squareroot of all elements 
print(np.sqrt(b))

# to get standard deviation
print(np.std(b))

# to get log of every element
print(np.log(b))

# pi in numpy
print(np.pi)

# sin function
print(np.sin(np.pi/2))

# using matplotlib 
a = np.arange(1,11)
b = np.arange(10,110,10)
plt.figure(figsize=(6,6))
plt.plot(a,b)
plt.show()

# printing sin function on graph
x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)
plt.figure(figsize=(6,6))
plt.plot(x,y)
plt.show()

# to get random array of specific no. of element
print(np.random.random(1))
print(np.random.random(2))

# to get random array of M x N elements
print(np.random.random((2,2)))

# to get random integer from a specific range
print(np.random.randint(1,10))

# to get random array of M x N with specific range of integers
print(np.random.randint(1,10,(2,2)))

# to get random array of float
print(np.random.rand(2,2))

# to get random array of float with negative number also
print(np.random.randn(2,2))

# to get random element from a array 
a = np.arange(2,100,5)
print(np.random.choice(a))
