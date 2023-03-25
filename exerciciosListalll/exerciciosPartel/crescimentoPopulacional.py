qTeste = int(input())
lista = []

for i in range(qTeste):
    c = 0
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    porA = ((pa * g1) // 100) + pa
    porB = ((pb * g2) // 100) + pb
    porA = int(porA)
    porB = int(porB)
    while porA <= porB:
        porA = ((porA * g1) // 100) + porA
        porB = ((porB * g2) // 100) + porB
        c += 1
        if c > 100:
            break

    c += 1
    lista.append(c)

for i in range(qTeste):
    if lista[i] > 100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % lista[i])