import sqlite3

conn = sqlite3.connect('BD_Dany_trab2AV1.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE PECAS(
    id_peca INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_peca TEXT NOT NULL,
    peso_peca FLOAT NOT NULL,
    cor_peca TEXT NOT NULL 
);
""")

cursor.execute("""
CREATE TABLE DEPOSITO(
    id_deposito INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_deposito TEXT NOT NULL,
    end_deposito TEXT NOT NULL 
);
""")

cursor.execute("""
CREATE TABLE FORNECEDOR(
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    end_fornecedor TEXT NOT NULL 
);
""")

cursor.execute("""
CREATE TABLE PROJETO(
    id_projeto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_projeto TEXT NOT NULL,
    orcamento_projeto FLOAT NOT NULL 
);
""")

cursor.execute("""
CREATE TABLE FUNCIONARIO(
    id_funcionario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_funcionario TEXT NOT NULL,
    cidade_funcionario TEXT NOT NULL,
    salario_funcionario FLOAT NOT NULL,
    telefone_funcionario TEXT NOT NULL 
);
""")

cursor.execute("""
CREATE TABLE DEPARTAMENTO(
    id_departamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_departamento TEXT NOT NULL,
    setor_departamento TEXT NOT NULL 
);
""")


conn.close()