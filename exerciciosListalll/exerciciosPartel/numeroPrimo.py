q = int(input())

for i in range(q):
    n = int(input())
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c != 2:
        print("%d nao eh primo" % n)
    elif c == 2:
        print("%d eh primo" % n)