import numpy as np

w=[(8-12)*15,(11-12)*15]
print(w)

def f(x):
    f=np.zeros(2)
    f[0]=4921*(np.sin(x[0]*np.pi/180)*np.sin(x[1]*np.pi/180)+np.cos(x[0]*np.pi/180)*np.cos(x[1]*np.pi/180)*np.cos(w[0]*np.pi/180))-2527.967
    f[1]=4921*(np.sin(x[0]*np.pi/180)*np.sin(x[1]*np.pi/180)+np.cos(x[0]*np.pi/180)*np.cos(x[1]*np.pi/180)*np.cos(w[1]*np.pi/180))-4611.454
    return f

x0=[0,-10]

print(f(x0))

def SubSuc(L,bs):
  n=bs.size
  xs=np.zeros(n)
  for i in range(n):
    xs[i] = (bs[i] -L[i,:i]@xs[:i])/L[i,i]
  return xs

def SubRet(U,bs):
  n=bs.size
  xs=np.zeros(n)
  for i in reversed(range(n)):
    xs[i] = (bs[i] -U[i,i+1:]@xs[i+1:])/U[i,i]
  return xs

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

def Sistema_Nao_L_Newton(f,x,tol,kmax):
    def jacobiana(f,x):
        h=1.0e-4
        n = len(x)
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
          return x
          break
    #else:
    print('nao convergiu')
    x = None
    return x

print(Sistema_Nao_L_Newton(f,x0,1e-16,100))