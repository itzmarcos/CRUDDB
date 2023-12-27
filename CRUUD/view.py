import sqlite3 as lite

con = lite.connect('dados.db')

#CRUD

def inserir_from(i):
    with con: 
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, valor_da_compra) VALUES (?,?)"
        cur.execute(query,i)


def att_(i):
    with con: 
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, valor_da_compra=? WHERE ID=?"
        cur.execute(query,i)


def deletar_from(i):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)


def ver_from():
    ver_dados = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados