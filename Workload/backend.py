import sqlite3

def connect():
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, ratio integer)")
    conn.commit()
    conn.close()

def insert(title,ratio):
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?)",(title,ratio))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",ratio=""):
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR ratio=?", (title,ratio))
    rows=cur.fetchall()
    conn.close() 
    return rows

def delete(id):
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()  

def update(id,title,ratio):
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, ratio=? WHERE id=?",(title,ratio,id))
    conn.commit()
    conn.close() 

def ratio_everyone():
    conn=sqlite3.connect("workload.db")
    cur=conn.cursor()
    cur.execute("SELECT SUM(ratio) FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
