import numpy as np

def SubRet(U,bs):
    n=bs.size
    xs=np.zeros(n)
    for i in reversed(range(n)):
      xs[i] = (bs[i] -U[i,i+1:]@xs[i+1:])/U[i,i]
    return xs

def ElimGauss(inA, inbs):
  A = np.copy(inA)
  bs = np.copy(inbs)
  n = bs.size
  for j in range(n-1):
    for i in range(j+1,n):
        m = A[i,j]/A[j,j]
        A[i,j:] -= m*A[j,j:]
        bs[i] -= m*bs[j]
  xs = SubRet(A,bs)
  return xs

def solucao_teste(Metodo,A,bs):
    xs = Metodo(A,bs); print(xs)
    xs =np.linalg.solve(A,bs); print(xs)

A = np.array([[4, 3, -5],
              [-2, -4, 5],
              [8, 8, 0]], dtype= float)
y = np.array([2, 5, -3], dtype=float)
#y = np.transpose(y)
print(A, "\n", y)
solucao_teste(ElimGauss,A,y)