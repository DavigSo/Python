m = []
op = input()

for i in range(12):
    m.append([])

    for j in range(12):
        a = float(input())
        m[i].append(a)

if op == "S":
    s = 0
    cont = 11
    for i in range(11, 0, -1):
        for j in range(0, cont):
            s += m[i][j]
        cont -= 1
    print("%.1f" % s)
elif op == "M":
    s = 0
    cont = 11
    cont2 = 0
    for i in range(11, 0, -1):
        for j in range(0, cont):
            s += m[i][j]
            cont2 += 1
        cont -= 1

    media = s / (cont2)
    print("%.1f" % media)