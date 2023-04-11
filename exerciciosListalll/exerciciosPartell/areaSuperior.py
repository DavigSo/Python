m = []
op = input()

for i in range(12):
    m.append([])

    for j in range(12):
        n = float(input())
        m[i].append(n)

s = 0
ct = 0
inf = 1
sup = 11

for i in range(0, 5):
    for j in range(inf, sup):
        s += m[i][j]
        ct += 1
    inf += 1
    sup -= 1

media = s / ct

if op == "S":
    print("%.1f" % s)
elif op == "M":
    print("%.1f" % media)