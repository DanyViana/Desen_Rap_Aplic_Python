import sqlite3

conn = sqlite3.connect('BD_Dany_trab2AV1.db')

cursor = conn.cursor()

print('Peças:')
cursor.execute("""
SELECT * FROM PECAS;""")
for linha in cursor.fetchall():
    print(linha)

print('Depósitos:')
cursor.execute("""
SELECT * FROM DEPOSITO;""")
for linha in cursor.fetchall():
    print(linha)

print('Fornecedores:')
cursor.execute("""
SELECT * FROM FORNECEDOR;""")
for linha in cursor.fetchall():
    print(linha)

print('Projetos:')
cursor.execute("""
SELECT * FROM PROJETO;""")
for linha in cursor.fetchall():
    print(linha)

print('Funcionários:')
cursor.execute("""
SELECT * FROM FUNCIONARIO;""")
for linha in cursor.fetchall():
    print(linha)

print('Departamentos:')
cursor.execute("""
SELECT * FROM DEPARTAMENTO;""")
for linha in cursor.fetchall():
    print(linha)

conn.close()
