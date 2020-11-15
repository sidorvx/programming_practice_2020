import numpy as np
import random

a = np.array([1, 12, 2, 34, 1])
b = np.array([1, 2])
print(a[~np.isin(a, b)])


b = np.array(['Note', 'Pan', 'Water', 'Potato', 'Melon'])

a = np.array([random.choice(b) for _ in range(2)])

print('Already buy: ', *a)

print('Need:', *b[~np.isin(b, a)])