from funcoes import Funcoes

agenda = []
favoritos = []

print("-----olá seja Bem vindo a agenda telefonica-----")

while True:
  print("[1] - listar contato;")
  print("[2] - buscar contato")
  print("[3] - modificar contato")
  print("[4] - eliminar contato")
  print("[5] - Imprimir todos os contatos")
  print("[6] - Imprimir os favoritos")
  print("[7] - Sair")

  opc = int(input("digite a opção que deseja : "))

  if opc == 1:
    nome = input("tecle o seu nome:")
    tele = int(input("tecle o seu telefone:"))
    cidade = input("tecle a sua cidade:")
    agenda.append(Funcoes.cadastrar(nome, tele, cidade))
    fav = int(input("tecle [1] Para adicionar aos favoritos"))
    fav.append(Funcoes.cadastrar(nome, tele, cidade))
  
  elif opc == 2:
    pesquisar = input("tecle o nome para concluir a pesquisa:")
    if pesquisar in agenda:
      print(f'{pesquisar} faz parte da agenda telefonica')
    else:
      print(pesquisar, "não faz parte da agenda telefonica")
  
  elif opc == 3:
    nome = input("tecle o nome que deseja alterar:")
    agenda.pop(nome)
    novoContato = input("Qual nome irá substituir?")
    agenda.append(novoContato)

  elif opc == 4:
    nome = input('tecle o nome para a pesquisa:')
    print(Funcoes.excluirNome(agenda, nome,))
  
  elif opc == 5:
    Funcoes.imprimaTodos(agenda)
  
  elif opc == 6:
    Funcoes.imprimaFavoritos(favoritos)
    
  elif opc == 7:
    break
    
  else:
    print("Digite um número que esteja nas opções!")

print("Obrigado por usar a nossa agenda!")
