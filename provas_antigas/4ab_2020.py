import numpy as np

#f é a função
#a e b são os chutes 
# tol eh a tolerancia
 
def bisec(f, a, b, tol):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception("Não há um número ímpar de raízes entre a e b.\n")

  # Ponto médio
  m = (a + b)/2

  if abs(f(m)) < tol:
    return m
  
  if np.sign(f(m)) == np.sign(f(a)):
    return bisec(f, m, b, tol)
  elif np.sign(f(m)) == np.sign(f(b)):
    return bisec(f, a, m, tol)

def f(x):
    G = 6.67*10**-11
    mt=5.98*10**24
    ms= 1.98*10**30
    R = 1.49 * 10**11
    T = 3.15576 * 10**7
    w = 2*np.pi/T
    return G*mt/(R-x*10**11)**2 + x*10**11*w**2 - G*ms/(x*10**11)**2

r1 = bisec(f, 0.1, 1.491, 0.001)
print("r1 =", r1)

print("f(r1) =", f(r1))

r2 = bisec(f, 1.13325, 1.48325, 2**-30)
print("r2 =", r2)
print("f(r2) =", f(r2))