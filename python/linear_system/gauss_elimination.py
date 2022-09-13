import numpy as np

def gauss_elim(A, B):
    a = np.copy(A)
    b = np.copy(B)

    n = len(a)
    x = np.zeros(n, float)

    # Eliminação
    for k in range(n-1):
        for i in range(k+1, n):
            m = a[i, k]/a[k, k]
            for j in range(k, n):
                a[i, j] -= m*a[k, j]
            b[i] -= m*b[k]

    # Retrossubstituição
    x[n-1] = b[n-1]/a[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum -= a[i, j]*x[j]
        x[i] = sum/a[i, i]

    return x

A = np.array([[4, 3, -5], 
              [-2, -4, 5], 
              [8, 8, 0]],dtype=float)
y = np.array([2, 5, -3],dtype=float)
y = np.transpose(y)

a = gauss_elim(A, y)
print(a)