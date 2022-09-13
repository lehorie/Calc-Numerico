import numpy as np

#transforma uma matriz simetrica A (= A^T)
#em uma matriz A = LDL^T
#os valores estarão todos na mesma matriz.
#a diagonal principal será a matriz diagonal D
#a parte triangular inferior L e assim por diante.

def LDLT(A):
    a=A.copy()
    n=len(a)
    for k in range(n-1):#resolve o sistem Lv=A
        for i in range(k+1,n):
            m=a[i,k]/a[k,k]
            a[i,k+1:n] = a[i,k+1:n] - m*a[k,k+1:n]
            a[i,k]=m
        for i in range(k+1,n):
            a[k,i]=a[i,k]
    #for j in range(n):  
        #a[j,j+1:n] = a[j,j+1:n]/a[j,j]
    return a

#exemplo
A=np.array([[10, 20, 30],[20,45,80],[30,80,171]])
print(A)
LDLT= LDLT(A)
print(LDLT)