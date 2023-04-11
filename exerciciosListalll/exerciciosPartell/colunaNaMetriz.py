cl = int(input())
op = input()

m = []

for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)

if op == "S":
    s = 0

    for linha in range(12):
        s += m[linha][cl]
    print(s)
elif op == "M":
    media = 0
    s = 0

    for linha in range(12):
        s += m[linha][cl]
    media = s / 12
    print("{:.1f}".format(media))