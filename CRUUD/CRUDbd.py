import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor_da_compra DECIMAL)")