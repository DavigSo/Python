import math

primeiraLinha = input().split()
segundaLinha = input().split()

x1, y1 = primeiraLinha
x2, y2 = segundaLinha

distancia = math.sqrt(((float(x2) - float(x1)) ** 2) + (float(y2) - float(y1)) ** 2)
print("%.4f" % distancia)
