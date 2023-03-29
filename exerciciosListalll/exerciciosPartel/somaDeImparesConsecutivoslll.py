q = int(input())

for i in range(0, q):
    a, b = input().split()
    a = int(a)
    b = int(b)

    s = 0

    x = 1
    while x <= b:
        if a % 2 != 0:
            s += a
            x += 1

            a += 1
        elif a % 2 == 0:
            a += 1

    print(s)