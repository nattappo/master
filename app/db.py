import sqlite3

def f():
    con = sqlite3.connect('pusdu.sqlite3')
    with con:
        cur = con.cursor()
        cur.execute('Select * from Gpus')
        rows = cur.fetchall()
        print (rows)


    

f()