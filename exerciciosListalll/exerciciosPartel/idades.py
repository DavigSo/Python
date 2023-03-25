m = 0
c = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        m += idade
        c += 1
print("%.2f" % (m / c))