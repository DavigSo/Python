n = int(input())

anos = n // 365
n = n - anos * 365

mes = n // 30
n = n - mes * 30

dias = n

print("{} ano(s)".format(anos))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dias))
