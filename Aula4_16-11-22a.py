#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: estabelecer uma 
#conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando sql do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o. passo: executar o comando sql no cursor(sqlite)
cursor.execute(sql)

#6o. passo: exibir a consulta com a tabela e coluna do banco de dados
print ("(cod, nome, nome civil, tipo:)")
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"nome: {pessoa[1]} é {pessoa[3]} /n")

for pessoa in pessoas:
  print(f"nome real do(a) {pessoa[1]} é {pessoa[2]}")