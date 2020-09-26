import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 1)
plt.plot((np.log(x**2 + 1)*(np.exp(-np.abs(x)/10)))/np.log((1+np.tan(x))*(1/(1+np.sin(x)*np.sin(x)))))
plt.show()