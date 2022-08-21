#comando para baixar a biblioteca Sqlite3:
# pip install db-sqlite3

import sqlite3




#criando banco de dados
banco = sqlite3.connect("primeiro banco")

#vamos criar um cursor, ele permite executar os comandos para o banco de dados.
cursor = banco.cursor()

#criando a tabela a partir do cursor:
#OBS: caso ja tenha sido executada a linha para criar a tabela irá dar erro então comente a linha.

#cursor.execute("CREATE TABLE clientes (nome text, idade integer, email text)")








#INSERINDO DADOS NO BANCO
#cursor.execute("INSERT INTO clientes VALUES('Guilherme', 20,'guilherme@gmail.com')")

#cursor.execute("INSERT INTO clientes VALUES('Agatha', 20, 'agatha@gmail.com')")

#o comit confirma que estamos inserindo informações no banco
#use o nome do banco.commit
banco.commit()








#COMANDO PARA APAGAR DADOSDO BANCO APARTIR DO NOME:
#cursor.execute("DELETE FROM clientes where nome='Guilherme'")
#cursor.execute("DELETE FROM clientes where nome='Agatha'")








#COMANDO PARA VISUALIZAR OS DADOS DO BANCO:
cursor.execute('SELECT * FROM clientes')
print(cursor.fetchall())



'''OBS: alguns comandos podem gerar erro no código, principalmente se forrem comandos que so podem ser executados uma vez, 
tal como criar uma tabela especifica, inserir um dado eu uma coluna com parametro not null.
'''