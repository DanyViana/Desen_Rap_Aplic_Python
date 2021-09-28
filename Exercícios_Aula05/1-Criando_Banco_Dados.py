import sqlite3
conn = sqlite3.connect('aula05_BD.db') # nome escolhido pro banco de dados (eu q escolho)

print("Banco de dados aberto com sucesso")

# definindo um cursor

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATE NOT NULL  
);
""") #cria através de um comentário mesmo!!! não tem vírgula nesse último "criado_em"

print ('Tabela criada com sucesso.')

#desconectando... 

conn.close()