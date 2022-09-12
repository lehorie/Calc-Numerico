import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x,y)
plt.plot(x,y,'ro')
plt.xlabel('Eixo x')
plt.ylabel('eixo y')
plt.grid()
plt.show()