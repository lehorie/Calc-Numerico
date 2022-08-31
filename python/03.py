g = lambda h: math.pi*h**2*(9 - h)/90 - 1
dg = lambda h: math.pi*h*(6 - h)/30

def newton_method_iter(f, df, x_old, n):

    x_old = 2
    n = 3
    
    print("Estimativa inicial: h =", x_old, "\n")

  for i in range(0, n):
    x_new = x_old - f(x_old)/df(x_old)
    erro_rel = abs(x_new - x_old)/x_new
    print(f"Erro relativo após a iteração {i + 1}:", erro_rel, "\n")
    x_old = x_new

  return x_new

  resp = x_new

  print("O tanque deve ser enchido até a profundidade de", resp, "metros\n")