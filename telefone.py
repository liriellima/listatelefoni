class Telefone():
  def _init_(self, nome, telefone, cidade):
    self.__nome = nome
    self.__telefone = telefone
    self.cidade = cidade

  def getNome(self):
    return self.__nome
  
  def getTelefone(self):
    return self.__telefone

  def getCidade(self):
    return self.__cidade
