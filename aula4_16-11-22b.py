import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

#7o. passo: comando para inserir objeto
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo:
cursor.execute(sql)

#7o. passo: confirmar o INSERT com commit() e fechar o banco close()
conexao.commit()
conexao.close()

#6o. passo:


