#Importar arquivos de outros diretórios
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
poyatos = Pessoa (1, "Henrique Poyatos")
print(poyatos)

#Mostrar apenas o nome
print(poyatos.nome)
print("ACESSO AO BANCO: ")

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Carregar um lista com o banco de dados
pessoas = pessoaDAO.getAll(orderBy = True)
for pessoa in pessoas:
  print(pessoa)

#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(0, "Denzel Washington")
pessoaDAO.save(novo)

pessoas = pessoaDAO.getAll(orderBy = True)
for pessoa in pessoas:
  print(pessoa)