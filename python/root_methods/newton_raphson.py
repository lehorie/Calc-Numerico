import numpy as np

def newton(f, df, x0, tol):
    # output is an estimation of the root of f 
    # using the Newton Raphson method
    # recursive implementation
    if abs(f(x0)) < tol:
        return x0
    else:
        return newton(f, df, x0 - f(x0)/df(x0), tol)

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
estimate = newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)