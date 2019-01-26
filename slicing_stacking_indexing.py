import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

print(a[2, 1])  # element in 2nd row and 1st column

# Slicing
print(a[0:2, 1])  # [rows from 0 to 1, column index 1]

print(a[:, 1:])

# iterate
for row in a:
    print(row)

# iterate as single dimensional array
for x in a.flat:
    print(x)


# you can stack vertically one array over another
a = np.arange(6).reshape(3, 2)
b = np.arange(7, 13).reshape(3, 2)
c = np.vstack((a, b))
print(c)

# same way you can do it for horizontal
c = np.hstack((a, b))
print(c)
print()

# you can separate them horizontally as well
a = np.arange(9).reshape(3, 3)
print(a)
c = np.hsplit(a, 3)
for row in c:
    print(row)
print()

# you can separate them vertically as well
a = np.arange(9).reshape(3, 3)
print(a)
c = np.vsplit(a, 3)
for row in c:
    print(row)
print()

# boolean array
a = np.arange(12).reshape(4, 3)
print(a)
b = a < 6
print(b)
print(a[b])  # it will get index of where True is found in b, and it will return a for that matching index
a[b] = -1  # True element index are assigned -1 in a
print(a)


