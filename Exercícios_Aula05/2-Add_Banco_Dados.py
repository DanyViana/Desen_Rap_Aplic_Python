import sqlite3
conn = sqlite3.connect('aula05_BD.db') # nome escolhido pro banco de dados (eu q escolho)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Dany', 31, '12345678912', 'dany@estacio.com', '85-98846-8054', 'Fortaleza', 'CE', '2021-21-09')
""")

conn.commit()

conn.close()

