n = int(input())
x = input().split()

for i in range(n):
    x[i] = int(x[i])
m = x[0]
p = 0

for j in range(1, n):
    if x[j] < m:
        m = x[j]
        p = j

print("Menor valor: %d" % m)
print("Posicao: %d" % p)