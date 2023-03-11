print('Bem-vindo ao sistema de Ouvidoria!')
listaReclamacoes = []
opcao = 0

while True:
  print('-*-'*10)
  print('1 - Adicionar reclamações.')
  print('2 - Listar reclamações.')
  print('3 - Excluir reclamações.')
  print('4 - SAIR!')
  print('-*-'*10)

  opcao = int(input('Digite sua opção: '))
  if opcao == 1:
    print('Adicionar reclamações')
    e = input('Faça sua Ocorrência: ')
    listaReclamacoes.append(e)
  elif opcao == 2:
    print('Listar Reclamações')
    for elemento in listaReclamacoes:
     print(elemento)
  elif opcao == 3:
    print('Deseja excluir uma reclamação ou todas?')
    print('0 - Excluir todas')
    print('1 - Excluir uma')
    e = int(input())
    if e == 0:
      print('Todas as reclamações foram apagadas.')
      listaReclamacoes.clear()
    elif e == 1:
      print('Apagar ocorrência especifica')
      a = int(input('Qual a reclamação: '))
      listaReclamacoes.pop(a)
      for rec in listaReclamacoes:
        print(rec) 
  elif opcao == 4:
    print('Obrigado por usar nossa Ouvidoria')
    break