import numpy as np
def elimgauss_pivo(inA,inb):
    A = np.copy(inA)
    bs = np.copy(inb)
    n = bs.size
    for j in range(n-1):
      k = np.argmax(np.abs(A[j:,j])) + j
      if k != j:
        A[j,:], A[k,:] = A[k,:], A[j,:].copy()
        bs[j], bs[k] = bs[k], bs[j]
      for i in range(j+1,n):
        m = A[i,j]/A[j,j]
        A[i,j:] -= m*A[j,j:]
        bs[i] -= m*bs[j]
    xs =SubRet(A,bs)
    return xs

def SubRet(U,bs):
    n=bs.size
    xs=np.zeros(n)
    for i in reversed(range(n)):
      xs[i] = (bs[i] -U[i,i+1:]@xs[i+1:])/U[i,i]
    return xs

#Exemplo
def solucao_teste(Metodo,A,bs):
  xs = Metodo(A,bs); print(xs)
  xs =np.linalg.solve(A,bs); print(xs)

A = np.array([[4, 3, -5], 
              [-2, -4, 5], 
              [8, 8, 0]], dtype= float)

y = np.array([2, 5, -3],dtype=float)

solucao_teste(elimgauss_pivo, A, y)