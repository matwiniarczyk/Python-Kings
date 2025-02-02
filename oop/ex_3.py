from numbers import Number


class X:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        print('add')
        if isinstance(other, type(self)):
           return X(self.x + other.x)

        if isinstance(other, Number):
            return X(self.x + other)

        return NotImplemented

    def __radd__(self, other):
        print('radd')
        return self + other

    def __str__(self):
        return str(self.x)

x1 = X(1)
x2 = X(2)

print(x1)
print(42 + x2)

import numpy as np

z = np.array([1, 2, 3])
z2 = np.array([1, 2, 3])

print(z + z2)
