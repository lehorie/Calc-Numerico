import numpy as np

def lu_dec(A):
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    N = np.size(A, 0)

    for k in range(N):
        L[k, k] = 1
        U[k, k] = (A[k, k] - np.dot(L[k, :k], U[:k, k])) / L[k, k]
        for j in range(k+1, N):
            U[k, j] = (A[k, j] - np.dot(L[k, :k], U[:k, j])) / L[k, k]
        for i in range(k+1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U

A = np.array([[4, 3, -5], 
              [-2, -4, 5], 
              [8, 8, 0]])
(a,b) = lu_dec(A)
print(a, "\n", b, "\n")

c = (a,b) = lu_dec(A)
print(c)