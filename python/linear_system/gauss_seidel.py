import numpy as np

def SubSuc(L,bs):
  n=bs.size
  xs=np.zeros(n)
  for i in range(n):
    xs[i] = (bs[i] -L[i,:i]@xs[:i])/L[i,i]
  return xs

def sol_gaussseidel(A,b,x0,kmax=100):
  M =np.tril(A)
  for k in range(kmax):
    r = b - A@x0
    h = SubSuc(M,r)
    if np.linalg.norm(h) < 1e-16 + 1e-16*np.linalg.norm(x0):
      break
    x0 += h
  return x0

#Exemplo
A =np.array([[5,1,1],
            [3,4,1],
            [3,3,6]],dtype = float)
b=np.array([5,6,0],dtype = float)
x0=np.zeros((3),dtype = float)
x=sol_gaussseidel(A,b,x0)
print(x)