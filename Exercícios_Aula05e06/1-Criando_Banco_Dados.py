import sqlite3
conn = sqlite3.connect('aula05_BD.db') # nome escolhido pro banco de dados (eu que escolho)
# Connect é uma função global do conector para criar uma conexão com o banco de dados. Retorna um objeto do tipo Connection.
# Connection é uma classe utilizada para gerenciar todas as operações no banco de dados. Principais métodos: *Commit: confirma todas as operações pendentes; *Rollback: desfaz todas as operações pendentes. *Cursor e *Close: explicados mais a diante. 

print("Banco de dados aberto com sucesso")

# definindo um cursor: retorna um objeto do tipo Cursor: classe utilizada para enviar os comandos ao banco de dados. Principais métodos: *Execute: prepara e executa a operação passada como parâmetro; *Fetchone: retorna a próxima linha encontrada por uma consulta; *Fetchall: retorna todas as linhas encontradas por uma consulta. 

cursor = conn.cursor()

# Após a criação da conexão com o banco de dados através do Connect, utiliza a conexão para criar um cursos, que será utilizado para enviar comandos ao banco de dados. 

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
# Close: encerra a conexão com o banco de dados. 
