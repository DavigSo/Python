while True:
    n = int(input())

    s = 0
    i = 1

    if n != 0:
        while i <= 5:
            if n % 2 == 0:
                s += n
                n += 1
                i += 1
            else:
                n += 1

        print(s)
    elif n == 0:
        break
        