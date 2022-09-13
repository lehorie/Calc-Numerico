import numpy as np

def sol_jacobi(A,b,x0,kmax=100):
  d =np.diag(A)
  for k in range(kmax):
    r = b - A@x0
    h = r/d
    if np.linalg.norm(h) < 1e-16 + 1e-16*np.linalg.norm(x0):
      return x0
    x0 += h
  return x0

#exemplo
A = np.array([[10,2,1],
            [1,5,1],
            [2,3,10]],dtype=float)
b = np.array([7,-8,6],dtype=float)
x0 = np.array([0,0,0],dtype=float)
x=sol_jacobi(A,b,x0)
print(x)
