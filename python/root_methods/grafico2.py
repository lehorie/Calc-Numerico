import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.linspace(0.0, 5.0, 100)
plt.subplot(211)
plt.grid()
plt.plot(t1,f(t1))
plt.show()