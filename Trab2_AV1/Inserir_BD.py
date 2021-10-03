import sqlite3

conn = sqlite3.connect('BD_Dany_trab2AV1.db')

cursor = conn.cursor()

lista_pecas = [
    ('anilha', 2.5, 'vermelha'),
    ('trempe', 9.1, 'azul'),
    ('parafuso', 2, 'verde'),
    ('vidro', 10.3, 'lilas'),
    ('rebite', 0.2, 'preta')]

cursor.executemany("""
INSERT INTO PECAS (nome_peca, peso_peca, cor_peca)
VALUES (?,?,?)
""", lista_pecas)

lista_deposito = [
    ('LEROY','Rua da faculdade'),
    ('CASAS FREITAS','Rua do trabalho'),
    ('DO CHICO','Av Beira Mar'),
    ('DA MARIA','Av Silas'),
    ('DO VICTOR','Rua da Estácio')]

cursor.executemany("""
INSERT INTO DEPOSITO (nome_deposito,end_deposito)
VALUES (?,?)
""", lista_deposito)

lista_fornecerdor = [
    ('AÇO TUDO','Av Parque oeste'),
    ('CSP','BR116'),
    ('ZUFFER','Av Leste oeste'),
    ('USIPLAST','Av paulino rocha'),
    ('VICTOR','Rua da faculdade estácio')]

cursor.executemany("""
INSERT INTO FORNECEDOR (nome_fornecedor,end_fornecedor)
VALUES (?,?)
""", lista_fornecerdor)

lista_projeto = [
    ('proj do carlos', 1000.00),
    ('proj de redução', 123450.67),
    ('projeto do sac', 90876.45),
    ('proj do eproj', 456),
    ('projeto diretoria', 123.45)]

cursor.executemany("""
INSERT INTO PROJETO (nome_projeto,orcamento_projeto)
VALUES (?,?)
""", lista_projeto)

lista_funcionario =[
    ('Dany', 'Fortaleza', 7123.45, 'planejamento'),
    ('Lucas', 'Maranguape', 1789.87, 'almoxarifado'),
    ('Paulo', 'Fortaleza', 657.98, 'fiscal'),
    ('Victor', 'Maracanaú', 4564.90, 'qualidade'),
    ('Odecilia', 'Maranguape', 7654.98, 'rh')]

cursor.executemany("""
INSERT INTO FUNCIONARIO (nome_funcionario, cidade_funcionario, salario_funcionario, telefone_funcionario)
VALUES (?,?,?,?)
""", lista_funcionario)

lista_departamento = [
    ('dep do fiscal','fiscal'),
    ('vende tudo','comercial'),
    ('gestão de pessoas','rh'),
    ('planejamento','pcp'),
    ('ast','pos vendas')]

cursor.executemany("""
INSERT INTO DEPARTAMENTO (nome_departamento,setor_departamento)
VALUES (?,?)
""", lista_departamento)


conn.commit()

conn.close()