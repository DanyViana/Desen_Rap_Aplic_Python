import sqlite3

conn = sqlite3.connect('aula05_BD.db') #conectando ao banco de dados

cursor = conn.cursor() #cursor que irá enviar o comando para o banco de dados

cursor.execute("""
SELECT * FROM clientes;""")
for linha in cursor.fetchall():
    print(linha)

#Fetchall: retorna todas as linhas encontradas por uma consulta

conn.close() #encerra a conexão com o banco de dados

#É possível fazer também consultas específicas:
# SELECT * FROM clientes WHERE idade > 35;  - nesse caso vai selecionar clientes com idade maior que 35 anos
# SELECT * FROM clientes WHERE cidade = 'Fortaleza'; - nesse caso vai selecionar clientes que moram na cidade de Fortaleza
# SELECT nome, cidade FROM clientes; - nesse caso vai selecionar somente as colunas de nome e cidade
