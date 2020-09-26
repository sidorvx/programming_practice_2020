import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-20, 20, 1)
y = eval(input())
with plt.xkcd():
    plt.plot(x, y)
plt.show()