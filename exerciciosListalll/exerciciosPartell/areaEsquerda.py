op = input()

s = 0
fora = 12
dentro = 0
mudar = False

qtd = 0
naoEntra = fora
entra = dentro

for i in range(144):
    valor = float(input())

    if mudar:
        if naoEntra + entra == 0:
            fora += 1
            dentro -= 1
            naoEntra = fora
            entra = dentro

        if entra > 0:
            entra -= 1
            s += valor
            qtd += 1
            continue

        if naoEntra > 0:
            naoEntra -= 1
            continue
    else:
        if naoEntra + entra == 0:
            fora -= 1
            dentro += 1
            naoEntra = fora
            entra = dentro

        if entra > 0:
            if entra == 6:
                mudar = True
                entra -= 1
                naoEntra += 1
                dentro -= 1
                fora += 1

            entra -= 1
            s += valor
            qtd += 1
            continue

        if naoEntra > 0:
            naoEntra -= 1
            continue

if op == "S":
    print("%.1f" % s)
elif op == "M":
    print("%.1f" % (s / float(qtd)))