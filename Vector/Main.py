import numpy as np

class Vector(object):
    def __init__(self, array):
        self.array = np.array(array, dtype=float)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.array * other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.array * other
            except:
                return "Нельзя умножать на буква или символы"

        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other,
                                                                                                            np.ndarray):
            if len(self) == len(other):
                return self.array * other.array if isinstance(other, Vector) else self.array * other
            else:
                return 'Они должны быть одного размера'

    def module(self):
        return np.linalg.norm(self.array)

    def dot_product(self, other):
        return np.dot(self.array, other.array)

    def vector_product(self, other):
        if isinstance(other, Vector):
            return np.vdot(self.array, other.array)
        else:
            return 'Это должен быть вектор'

    def distance(self, other):
        if isinstance(other, Vector):
            return np.linalg.norm(self.array - other.array)
        else:
            return 'Это должен быть вектор'

a = Vector([1, 2, 3])
b = Vector([1, 1, 1])
print(a.module())
print(a.dot_product(b))
print(a.vector_product(b))
print(a.distance(b))