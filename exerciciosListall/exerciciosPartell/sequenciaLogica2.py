a, b = map(int, input().split())

n = []
primeiro = 0

i = 0

while i < b - a:
    for j in range(1, a + 1):
        n.append(i + 1)
        div = n[primeiro]
        n[primeiro] = str(n[primeiro])
        primeiro += 1
        i += 1

    primeiro = 0
    n = " ".join(n)
    print(n)
    n = []

r = b % a

if r == 0:
    for x in range(b - a, b):
        n.append(x + 1)
        n[primeiro] = str(n[primeiro])
        primeiro += 1
    n = " ".join(n)
    print(n)

if r != 0:
    for x in range(div, b):
        n.append(x + 1)
        n[primeiro] = str(n[primeiro])
        primeiro += 1
    n = " ".join(n)
    print(n)