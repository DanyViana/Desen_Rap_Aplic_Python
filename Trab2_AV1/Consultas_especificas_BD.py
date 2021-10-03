import sqlite3

conn = sqlite3.connect('BD_Dany_trab2AV1.db')

cursor = conn.cursor()

print('Peças com peso maior que 75 gramas:')
cursor.execute("""
SELECT * FROM PECAS WHERE peso_peca > 0.75 ;""")
for linha in cursor.fetchall():
    print(linha)

print('Projetos com orçamento menor que R$ 50.000,00:')
cursor.execute("""
SELECT * FROM PROJETO WHERE orcamento_projeto < 50000 ;""")
for linha in cursor.fetchall():
    print(linha)

print('Funcionários com salários maiores ou iguais a R$ 4.225,32:')
cursor.execute("""
SELECT * FROM FUNCIONARIO WHERE salario_funcionario >= 4225.32 ;""")
for linha in cursor.fetchall():
    print(linha)

print('Funcionários que residem em Maranguape:')
cursor.execute("""
SELECT * FROM FUNCIONARIO WHERE cidade_funcionario = 'Maranguape' ;""")
for linha in cursor.fetchall():
    print(linha)

print('Peças com cor azul:')
cursor.execute("""
SELECT * FROM PECAS WHERE cor_peca = 'azul' ;""")
for linha in cursor.fetchall():
    print(linha)

conn.close()