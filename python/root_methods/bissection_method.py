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
    return x**2 - 2

r1 = bisec(f, -1, 2, 2**-50)
print("r1 =", r1)
r01 = bisec(f, -1, 2, 2**-26)
print("r01 =", r01)

print("f(r1) =", f(r1))
print("f(r01) =", f(r01))