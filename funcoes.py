from telefone import Telefone

class Funcoes():
  def cadastrar(nome, telefone, cidade):
    return Telefone(nome, telefone, cidade)
    
  def excluirNome(listaTelefone, nome):
    if len(listaTelefone) != 0:
      cont = 0
      for tel in listaTelefone:
        if tel.getNome() == nome:
          listaTelefone.pop(cont)
          return "Contato {} removido com sucesso!".format(nome)
        else:
          return "Nome não encontrado!"

  def imprimaTodos(listaTelefone):
    for tel in listaTelefone:
      print('{} | {} | {}'.format(tel.getNome(), tel.getTelefone(),tel.getCidade()))

  def imprimaFavoritos(listaTelefone):
    for tel in listaTelefone:
      print('{} | {} | {}'.format(tel.getNome(), tel.getTelefone(),tel.getCidade()))
