import sqlite3

conn = sqlite3.connect('aula05_BD.db') #conectando ao banco de dados

cursor = conn.cursor() #criando o cursor que irá enviar o comando para o banco de dados

id_cliente = 4
nova_idade = 31
nova_cidade = 'Vila'

#Alterando os dados da tabela: 
cursor.execute("""
UPDATE clientes
SET idade = ?, cidade = ?
WHERE id = ?
""", (nova_idade, nova_cidade, id_cliente))

conn.commit()

print('Dados atualizados com sucesso!')

cursor.execute("""
SELECT * FROM clientes;""")
for linha in cursor.fetchall():
    print(linha)

conn.close()