import numpy as np
x = np.array((1, 10, 1000))
y = np.log((np.e**(1/np.sin(x)+1))/((5/4)+(1/x**15)))/np.log(1+x**2)
print(y)