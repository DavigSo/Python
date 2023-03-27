a = []

for i in range(100):
    n = float(input())
    a.append(n)
    if n <= 10.0:
        print("A[%d] = %.1f" % (i, n))