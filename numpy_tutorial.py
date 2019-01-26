import numpy as np
import time
import sys

"""

TOPIC - 1
---------
SPACE

numpy uses contiguous memory, while python list uses contiguous list of pointers pointing to the list elements

"""

# numpy array uses less space than regular list
lst = range(1000)
print(sys.getsizeof(5) * len(lst))

array = np.arange(1000)
print(array.size * array.itemsize)
print()

"""

TOPIC - 2 
---------
SPEED

"""

# how numpy is faster than regular
SIZE = 100000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
print("Python took : ", (time.time() - start)*1000)

# numpy array
start = time.time()
result = a1 + a2
print("numpy took: ", (time.time() - start)*1000)
print()
"""

TOPIC - 3 
---------
SIMPLE OPERATIONS

"""
a1 = np.array([1, 2, 3])
a2 = np.array([3, 5, 7])
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
print()
