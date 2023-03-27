q = int(input())
for i in range(q):
    n = int(input())
    s = 0
    c = 1
    while c < n:
        if n % c == 0:
            s += c
        c += 1
    if s == n:
        print("%d eh perfeito" % n)
    else:
        print("%d nao eh perfeito" % n)