op = input()
m = []

for i in range(12):
    m.append([])

    for j in range(12):
        num = float(input())
        m[i].append(num)

if op == "S":
    s = 0
    cont = 1

    for i in range(0, 11):
        for j in range(cont, 12):
            s += m[i][j]
        cont += 1
    print("%.1f" % s)
elif op == "M":
    s = 0
    cont = 1
    cont2 = 0

    for i in range(0, 11):
        for j in range(cont, 12):
            s += m[i][j]
            cont2 += 1
        cont += 1

    media = s / cont2
    print("%.1f" % media)