import numpy as np
def false(f, a, b, Tol, nmi):
    #f é a função
    #a e b são valores com raiz no meio
    #tol eh a tolerancia
    #nmi numero maximo de iteracoes
    middle = (a*abs(f(b))+b*abs(f(a)))/(abs(f(b))+abs(f(a)))
    dif = f(middle)
    k=0
    while(abs(b-a)/abs(a)>Tol):
        if(k> nmi - 1):
            print('Numero de interações maximo alcançado')
            break
        if(dif*f(a)<0):
            b = middle
        else:
            a = middle  
        middle = (a*abs(f(b))+b*abs(f(a)))/(abs(f(b))+abs(f(a)))
        dif = f(middle)
        k+=1
    print('o valor é %.8f'%f(middle))
    print('a raiz é %.10f' %middle)

def f(x): 
    return x**2 - 2

r1 = false(f, 2, -2, 2**-30, 100)
