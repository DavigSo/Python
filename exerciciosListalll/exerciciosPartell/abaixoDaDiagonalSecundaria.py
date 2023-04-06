op = input()

s = 0
fora = 0
dentro = 11
qtd = 0

naoEntra = fora
entra = dentro

for i in range(144):
    num = float(input())

    if entra > 0:
        entra -= 1
        s += num
        qtd += 1
        continue

    if naoEntra > 0:
        naoEntra -= 1
        continue

    if naoEntra + entra == 0:
        fora += 1
        dentro -= 1
        naoEntra = fora
        entra = dentro

if op == "S":
    print("%.1f" % s)
elif op == "M":
    print("%.1f" % (s / float(qtd)))