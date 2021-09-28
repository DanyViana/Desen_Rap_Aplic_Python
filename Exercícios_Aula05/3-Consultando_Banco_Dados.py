import sqlite3
conn = sqlite3.connect('aula05_BD.db')
cursor = conn.cursor()
cursor.execute("""
SELECT * FROM clientes;""")
for linha in cursor.fetchall():
    print(linha)

conn.close()