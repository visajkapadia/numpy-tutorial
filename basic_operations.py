import numpy as np

# one dimensional array
print("1D Array")
a = np.array([1, 2, 3])
print(a)
print(a[0])
print()

# two dimensional array
print("2D Array")
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

# how to print dimension of the array (using ndim)
print(a.ndim)

# What is the byte size of each element?
print(a.itemsize)

# what is data type? (int64 is 8 bytes, int32 is 4 bytes)
print(a.dtype)

# assign array with different data types
a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print(a)
print(a.itemsize)

# how many elements in the array?
print(a.size)

# Whats is number of (rows, columns)?
print(a.shape)

# How to create complex number array?
a = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
print(a)

# Create array of zeros with given shape
a = np.zeros((5, 3))
print(a)

# Create array of ones with given shape
a = np.ones((2, 3))
print(a)

# generate array based on range
a = np.arange(3, 8)
print(a)

a = np.arange(3)
print(a)

a = np.arange(2, 7, 2)  # range with step value
print(a)


# Generate N equally spaced numbers between range
# linearly spaced elements
a = np.linspace(1, 4, 4)  # 4 numbers between 1 and 4
print(a)

a = np.linspace(1, 5, 9)  # 9 numbers between 1 and 5
print(a)

# Reshape elements
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.shape)

a = a.reshape(2, 3)
print(a)
print(a.shape)

a = a.reshape(6, 1)
print(a)


# Turn any dimensional array into 1D array
a = a.ravel()
print(a)

"""

NOTE: ALL FUNCTIONS ABOVE WILL NOT ALTER ORIGINAL ARRAY, IT WILL RETURN NEW ARRAY

"""


"""

MATHEMATICAL FUNCTIONS
----------------------
(1) MIN
(2) MAX
(3) SUM
(4) SQRT
(5) Standard Deviation

"""

print(a.min())
print(a.max())
print(a.sum())
print(np.sqrt(a))
print(np.std(a))

# axis 0 and axis 1
"""
axis 0 is columns
axis 1 is rows

"""
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a.sum(axis=0))  # addition of all columns
print(a.sum(axis=1))  # addition of all rows



"""
Array operations
"""

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.dot(b))  # MATRIX MULTIPLICATION


