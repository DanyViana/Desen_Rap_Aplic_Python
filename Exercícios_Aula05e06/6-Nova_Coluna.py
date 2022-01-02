import sqlite3

conn = sqlite3.connect('aula05_BD.db') #conectando ao banco de dados

cursor = conn.cursor() #criando o cursor que vai enviar o comando para o banco de dados

cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()

print('Novo campo adicionado com sucesso!')

conn.close()