import math
import numpy as np
import pandas as pd

# Implementação do método de Newton-Raphson com 3 iterações
def newton_method_iter(f, df, x_old, n):
  print("Estimativa inicial: h =", x_old, "\n")

  for i in range(0, n):
    x_new = x_old - f(x_old)/df(x_old)
    erro_rel = abs(x_new - x_old)/x_new
    print(f"Erro relativo após a iteração {i + 1}:", erro_rel, "\n")
    x_old = x_new

  return x_new

# Fórmulas
g = lambda h: math.pi*h**2*(9 - h)/90 - 1
dg = lambda h: math.pi*h*(6 - h)/30

# Resposta
resp = newton_method_iter(g, dg, 2, 3)
print("O tanque deve ser enchido até a profundidade de", resp, "metros\n")