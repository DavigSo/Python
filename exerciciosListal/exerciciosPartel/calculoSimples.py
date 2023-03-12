CodigoPecas1, NumeroPecas1, PrecoPecas1 = input().split()
CodigoPecas2, NumeroPecas2, PrecoPecas2 = input().split()
NumeroPecas1 = int(NumeroPecas1)
NumeroPecas2 = int(NumeroPecas2)
PrecoPecas1 = float(PrecoPecas1)
PrecoPecas2 = float(PrecoPecas2)

valorpecas1 = NumeroPecas1 * PrecoPecas1
valorpecas2 = NumeroPecas2 * PrecoPecas2
valorFinal = valorpecas1 + valorpecas2

print("VALOR A PAGAR: R$ %.2f" % valorFinal)
