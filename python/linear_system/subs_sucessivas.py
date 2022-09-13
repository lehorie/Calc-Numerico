import numpy as np

#consegue resolver um sistema triangular inferior L =lower
def SubSuc(L,bs):
  n=bs.size
  xs=np.zeros(n)
  for i in range(n):
    xs[i] = (bs[i] -L[i,:i]@xs[:i])/L[i,i]
  return xs

#exemplo
def criarteste(n, val):
    #cria uma matriz de val até val + n^2, ou seja, vai ter n^2 elementos.
    #redimensiona para ficar uma matriz quadrada.
    A=np.arange(val,val + n*n).reshape(n,n)
    A =np.sqrt(A)
    #linha 0, todas as colunas
    bs=(A[0,:])**2.1
    return A,bs 
def solucao_teste(Metodo,A,bs):
  xs = Metodo(A,bs); print(xs)
  xs =np.linalg.solve(A,bs); print(xs)

A,bs =criarteste(4,21)
#triangulariza a matriz para lower
L=np.tril(A)
solucao_teste(SubSuc,L,bs)

C = np.arange(21,21 + 4*4).reshape(4,4)
#bs=(C[1:3,1:3])
print(C, "\n",  bs)
