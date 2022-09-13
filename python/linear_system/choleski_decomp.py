import numpy as np
import math

#A fatoração de Choleski é possível, 
# quando a matriz A é simetrica e definida e positiva, 
# ou seja dado um vetor x de ordem n, então x^TAx>0. 
# Logo A pode ser fatorado como  LL^T

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