import aula4_16_11_22c as bd

conexao, cursor = bd.conectar()

nome = input("informe o nome do herói/vilão")
nome_civil = input("input o nome civil do herói/vilão")
tipo_numerico = input("tecle 1 para herói e 2 para vilão")

#consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"

else:
  tipo = "Vilã(o)"

sql = f"INSERTO INTO pessoas (pessoas_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)
conexao.commit()
conexao.close()

