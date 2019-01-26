import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

# normal way iteration
for row in a:
    for cell in row:
        print(cell)
print()

# numpy way
for cell in a.flatten():
    print(cell)
print()

# nditer (printing normal row wise)
for cell in np.nditer(a, order='C'):
    print(cell)
print()

# nditer (for printing column wise, it is called Fortran order)
for cell in np.nditer(a, order='F'):
    print(cell)
print()

# nditer (for printing column wise, it is called Fortran order) BUT ENTIRE COLUMN not single element
for cell in np.nditer(a, order='F', flags=['external_loop']):
    print(cell)

# for squaring each element, modifying original array
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x * x
print(a)


b = np.arange(3).reshape(3, 1)
for x, y in np.nditer([a, b]):  # to do this shape should be same, or one of the dimension should be 1
    print(x, y)
