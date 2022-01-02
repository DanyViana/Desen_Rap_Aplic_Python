import sqlite3
conn = sqlite3.connect('aula05_BD.db') #Estabelecendo a conexão com o banco de dados. 

cursor = conn.cursor() #Cursos que irá enviar comandos para o banco de dados. 

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Dany', 31, '12345678912', 'dany@estacio.com', '85-98846-8054', 'Fortaleza', 'CE', '2021-21-09')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Phillip', 28, '12345678912', 'phillip@estacio.com', '85-99999-9999', 'Fortaleza', 'CE', '2022-02-01')
""")

#É possível inserir linha a linha dessa forma acima. Ou inserir através de uma lista como será mostrado abaixo: 

lista = [
    ('Amor', 28, '12345678912', 'amor@estacio.com', '85-99999-9999', 'Fortaleza', 'CE', '2022-02-01'),
    ('Danielly', 28, '12345678912', 'danielly@estacio.com', '85-99999-9999', 'Fortaleza', 'CE', '2022-02-01')
] 
#Não esqueça os () das listas!!! 
#Inserindo os dados na tabela:
cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)
#A quantidade de ? é de acordo com a quantidade de atributos de cada entidade. 

conn.commit() #Vai confirmar todas as operações realizadas. 

conn.close() #Encerra a conexão com o banco de dados. 

