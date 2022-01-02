import sqlite3

conn = sqlite3.connect('aula05_BD.db') #conectando ao banco de dados

cursor = conn.cursor() #criando o cursor que irá enviar o comando para o banco de dados

id_cliente = 3

#Excluindo um registro da tabela

cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

#Não esquece dessa vírgula!!!! Pra que ela serve? Boa pergunta! 

conn.commit()

print('Dados atualizados com sucesso!')

cursor.execute("""
SELECT * FROM clientes;""")
for linha in cursor.fetchall():
    print(linha)

conn.close()