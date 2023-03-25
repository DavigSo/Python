q = int(input())

for i in range(q):
    n = int(input())
    fibo = [0, 1]
    if n > 1:
        for j in range(2, n + 1):
            fibo.append(fibo[j - 2] + fibo[j - 1])

        print("Fib(%d) = %d" % (n, fibo[n]))
    elif n <= 1:
        print("Fib(%d) = %d" % (n, fibo[n]))