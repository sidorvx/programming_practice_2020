import numpy as np

def norm(mat):
    return mat / mat.max()

a = np.random.randint(0, 100, size=10)
print(a, norm(a), sep='\n')