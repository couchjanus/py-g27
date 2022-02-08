import sqlite3

db = './storages/blog.db'

with sqlite3.connect(db) as c:
    cur = c.cursor()
    cur.execute("SELECT * from blogs")
    res = cur.fetchall()
    
print(res)