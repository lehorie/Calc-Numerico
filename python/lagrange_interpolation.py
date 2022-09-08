from re import I
import numpy as np
import matplotlib.pyplot as plt
x = np.array([0, 20, 40, 60, 80, 100],float)
y = np.array([1, 2, 3, 4, 5, 6], float)

xplt = np.linspace(x[0], x[-1])
yplt = np.array([], float)
for xp in xplt: 
    yp = 0

    for xi, yi in zip(x,y):
        yp += yi * np.product((xp - x[x != xi])/(xi - x[x != xi]))
    yplt = np.append(yplt, yp)

plt.plot(x, y, 'ro', xplt, yplt, 'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()