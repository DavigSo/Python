n = []
a = float(input())

for i in range(100):
    if i == 0:
        metade = a
        n.insert(i, metade)
    else:
        metade /= 2
        n.insert(i, metade)

for i in range(100):
    print("N[%d] = %.4f" % (i, n[i]))