a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    if a % b == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif a < b:
    if b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif a == b:
    print("Sao Multiplos")
