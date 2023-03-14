salario = float(input())
if salario <= 400.00:
  sajustado = salario * 1.15
  reajuste = sajustado - salario
  percentual = 15
elif 400.01 <= salario <= 800.00:
  sajustado = salario * 1.12
  reajuste = sajustado - salario
  percentual = 12
elif 800.01 <= salario <= 1200.00:
  sajustado = salario * 1.10
  reajuste = sajustado - salario
  percentual = 10 
elif 1200.01 <= salario <= 2000.00:
  sajustado = salario * 1.07
  reajuste = sajustado - salario
  percentual = 7
elif salario > 2000.00:
  sajustado = salario * 1.04
  reajuste = sajustado - salario
  percentual = 4
print("Novo salario: {:.2f}".format(sajustado))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))