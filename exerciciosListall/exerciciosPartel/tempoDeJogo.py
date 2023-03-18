hi, hf = input().split()

hi = int(hi)
hf = int(hf)
if hi < hf:
  tempo = hf - hi
  print("O JOGO DUROU {} HORA(S)".format(tempo))
else:
  tempo = (24 - hi) + hf
  print("O JOGO DUROU {} HORA(S)".format(tempo))