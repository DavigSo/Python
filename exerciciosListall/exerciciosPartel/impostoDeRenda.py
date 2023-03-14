renda = float(input())

if renda <= 2000.00:
  imposto = 0
  print("Isento")
elif 2000.00 < renda <= 3000.00:
  iRenda8 = renda - 2000.00
  imposto = iRenda8 * (8 / 100)
  print('R$ {:.2f}'.format(imposto))
elif 3000.00 < renda <= 4500.00:
  iRenda8 = (8 / 100) * (1000.00)
  iRenda18 = renda - 3000.00
  imposto = iRenda18 * (18 / 100) + iRenda8
  print('R$ {:.2f}'.format(imposto))
elif renda > 4500.00:
  iRenda8 = (8 / 100) * (1000.00)
  iRenda18 = (18 / 100) * (1500.00)
  iRenda28 = renda - 4500.00
  imposto = iRenda18 + iRenda8 + iRenda28 * (28 / 100)
  print('R$ {:.2f}'.format(imposto))