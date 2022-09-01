# Bibliotecas
import math
import numpy as np
import pandas as pd

# Implementação do método de Newton-Raphson com 3 iterações
def newton_method_iter(f, df, x_old, n):
  print("Estimativa inicial: h =", x_old, "\n")

  for i in range(0, n):
    x_new = x_old - f(x_old)/df(x_old)
    erro_rel = abs(x_new - x_old)/x_new
    print(f"Erro relativo após a iteração {i + 1}:", erro_rel, "\n")
    x_old = x_new

  return x_new

# Implementação do método de Newton-Raphson com tolerância
def newton_method_tol(f, df, x0, tol):
  if abs(f(x0)) < tol:
    return x0
  else:
    return newton_method_tol(f, df, x0 - f(x0)/df(x0), tol)

# Implementação do método da bissecção
def bisec(f, a, b, tol):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception("Não há um número ímpar de raízes entre a e b.\n")

  # Ponto médio
  m = (a + b)/2

  if abs(f(m)) < tol:
    return m
  
  if np.sign(f(m)) == np.sign(f(a)):
    return bisec(f, m, b, tol)
  elif np.sign(f(m)) == np.sign(f(b)):
    return bisec(f, a, m, tol)

# Implementação da Eliminação de Gauss
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

# Implementação da Eliminação com Pivotamento
def pivot_elim(A, B):
    a = np.copy(A)
    b = np.copy(B)

    n = len(a)
    x = np.zeros(n, float)

    # Eliminação e Pivotamento
    for j in range(n-1):
      k = np.argmax(np.abs(A[j:,j])) + j
      if k != j:
        A[j,:], A[k,:] = A[k,:], A[j,:].copy()
        b[j], b[k] = b[k], b[j]
      for i in range(j+1,n):
        m = A[i,j]/A[j,j]
        A[i,j:] -= m*A[j,j:]
        b[i] -= m*b[j]

    # Retrossubstituição
    x[n-1] = b[n-1]/a[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum -= a[i, j]*x[j]
        x[i] = sum/a[i, i]

    return x

# Implementação da Decomposição LU
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

for n in range(2, 16):
  A = np.zeros((n, n))
  B = np.zeros((n, 1))

  for i in range(0, n):
    for j in range(0, n):
      A[i, j] = (i + j + 1)**(-1)
      B[i, 0] += A[i, j]

  resp = gauss_elim(A, B)

  print(f"A solução para n = {n} é", resp, "\n")