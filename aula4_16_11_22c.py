import sqlite3

#8o. passos: passos 2 e 3 virarão função conectar()
def conectar():
  conexao = sqlite3.connect("dc_universe.db")
  
  cursor = conexao.cursor()

  return conexao, cursor