import numpy as np

def SubRet(U,bs):
    n=bs.size
    xs=np.zeros(n)
    for i in reversed(range(n)):
      xs[i] = (bs[i] -U[i,i+1:]@xs[i+1:])/U[i,i]
    return xs

#Exemplo
def criarteste(n, val):
  A=np.arange(val,val + n*n).reshape(n,n)
  A =np.sqrt(A)
  bs=(A[0,:])**2.1
  return A,bs

def solucao_teste(Metodo,A,bs):
  xs = Metodo(A,bs); print(xs)
  xs =np.linalg.solve(A,bs); print(xs)


A,bs =criarteste(4,21)
#triangulariza a matriz para upper
U = np.triu(A)
solucao_teste(SubRet, U,bs)