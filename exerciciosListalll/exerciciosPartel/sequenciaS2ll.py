n = 1
s = 0

for i in range(1, 40, 2):
    result = i / n
    s = s + result
    n = n * 2

print("%.2f" % s)