n = int(input())
hora = n // 60**2
n = n - hora * 60**2

minuto = n // 60
n = n - minuto * 60

segundo = n

print("{}:{}:{}".format(hora, minuto, segundo))
