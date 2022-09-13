import numpy as np

#resolve um sistema do tipo (L*L^T)x = b
def Sol_choleski(L,b):
    n = len(b)
    x=np.zeros((n))
    y=np.zeros((n))
    # Solução de [L]{y} = {b}
    for k in range(n):
      y[k] = (b[k] - L[k,0:k]@y[0:k])/L[k,k]
    # Solução [L_T]{x} = {y}
    for k in range(n-1,-1,-1):
       x[k] = (y[k] - L[k+1:n,k]@x[k+1:n])/L[k,k]
    return x

#exemplo
#pegando uma matriz de cholenski
import math
def choleski(A):
    L=A.copy()
    n = len(A)
    for k in range(n):
        try:
            L[k,k] = math.sqrt(L[k,k]- L[k,0:k]@L[k,0:k])
        except ValueError:
            print('matriz não é definita e positiva')
        for i in range(k+1,n):
            L[i,k] = (L[i,k] - L[i,0:k]@L[k,0:k])/L[k,k]
    for k in range(1,n): L[0:k,k] = 0.0
    return L

A =np.array([[1,2,3,4],[2,20,18,16],[3,18,19,21],[4,16,21,33]])
L = choleski(A)
print(L)

#resolve o sistema de cholenski
b=np.array([4,6,8,8])
x=Sol_choleski(L,b)
print(x)