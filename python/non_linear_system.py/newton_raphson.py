import numpy as np

def Sistema_Nao_L_Newton(f,x,tol=1.0e-9, kmax=100):
    def jacobiana(f,x):
        h=1.0e-4
        n=len(x)
        J =np.zeros((n,n))
        f0 =f(x)
        for i in range(n):
            x_original =x[i]
            x[i] = x_original +h
            f1 = f(x)
            x[i] = x_original
            J[:,i] = (f1-f0)/h 
        return J,f0
    for k in range(kmax):
        J,f0 =jacobiana(f,x)
        if np.linalg.norm(f0)/len(x) < tol: return x
        dx= elimgauss_pivo(J,-f0)
        x= x +dx
        if np.linalg.norm(dx) < tol*max(max(abs(x)),1.0):
          #return x
            break
    print('não convergiu')
    #else: 
     #     x = None
    return x
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

#exemplo 
def f(x):
  f=np.zeros(len(x))
  f[0]= x[0]**2 + 4*x[1]**2 -5
  f[1]=2*x[0]**2 - 2*x[0] -3*x[1] -2.5
  return f

x0 =np.array([0,0])
x=Sistema_Nao_L_Newton(f,x0)
print(x)

#chute nao deu certon entao

x_chute = [[1.5,1.5],[-0.5,1.5]]
for x_chute in x_chute:
  x = Sistema_Nao_L_Newton(f,x_chute)
  print(x)

#comparando a resposta
from scipy import optimize

x=optimize.fsolve(f,[1.5,1.5])
x2=optimize.fsolve(f,[-1.0,1.0])
print(x)
print("\n",x2)