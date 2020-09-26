import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2, 2, 0.001)
n = 10
a = 3
b = 1/2
S = 0
for i in range(0, n+1): S += np.power(b, i)*np.cos(np.power(a, i)*np.pi*x)
plt.plot(x, S)
plt.show()