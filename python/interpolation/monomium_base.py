import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import pandas as pd

def lagrangenp(x,y):
    n=len(x) # grau do polinomio n-1
    l=np.zeros(n)
    P=[]
    L = np.zeros((n,n))
    for m in range(n):
      P=[1]
      for k in range(n):
        if k != m: P = poly.polymul(P,[ -x[k],1])/(x[m] -x[k]) # no matlab equivalente a função conv()
      L[m,:] = P
      l = l + y[m]*P    
    return l,L

#x=[-2,-1,1,2]
#y=[-6,0,0,6]
x = [-1, 0, 3]
y = [15, 8,-1]
l,L=lagrangenp(x,y)
Tabela=pd.DataFrame(L)
print(l)
print(L)
print(Tabela)