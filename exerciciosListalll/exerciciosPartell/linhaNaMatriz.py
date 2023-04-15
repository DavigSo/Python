l = int(input())
op = input()

m = []

for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        n = float(input())
        m[i].append(n)

if op == "S":
    s = 0

    for elm in m[l]:
        s += elm

    print(s)
elif op == "M":
    media = 0
    s = 0

    for elm in m[l]:
        s += elm

    media = s / 12
    print(media)